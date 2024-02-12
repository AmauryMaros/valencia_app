import streamlit as st
import pandas as pd
import base64

st.sidebar.subheader("Contact")
st.sidebar.write("mfrance@som.umaryland.edu")

st.header("Qiime2 conversion", divider = 'grey')

st.markdown('<div style="text-align: justify;">\
            This script takes ouput from qiime2 and converts it to a format suitable for VALENCIA. \
            The two files expected as input are the ASV taxon names key and the ASV read count table. \
            The expected output is a new table which contains the samples as rows and the condensed taxa as columns. \
            This file can be used as input to VALENCIA. The second file provides a link between the original taxa names and the condensed names.</div>',
            unsafe_allow_html = True)

@st.cache_data
def convert_df(df, col):
   return df.to_csv(index=col).encode('utf-8')

st.divider()

st.subheader("Inputs")

input_1 = st.file_uploader("ASV taxon names key")
input_2 = st.file_uploader("ASV read count table")

if input_1 is not None and input_2 is not None :

    taxon_key = pd.read_csv(input_1,sep=",",index_col=0)
    taxon_key.columns = ['k','p','c','o','f','g','s']
    taxon_key = taxon_key[taxon_key.columns[::-1]]

    counts_table = pd.read_csv(input_2,sep=",",index_col=0)

    run = st.button("Run conversion")

    if run :
        def taxon_condense(row):

            row = row.T

            first_nonan = row.first_valid_index()

            if first_nonan == 's':
                if row.loc[['g']].values[0] in ['Lactobacillus','Prevotella','Gardnerella','Atopobium','Sneathia']:
                    taxon_name = "%s_%s" %(row.loc[['g']].values[0],row.loc[['s']].values[0])
                else:
                    taxon_name = "g_%s" %(row.loc[['g']].values[0])
            elif first_nonan == 'g':
                taxon_name = "g_%s" %(row.loc[['g']].values[0])
            elif first_nonan == 'f':
                taxon_name = "f_%s" %(row.loc[['f']].values[0])
            elif first_nonan == 'o':
                taxon_name = "o_%s" %(row.loc[['o']].values[0])
            elif first_nonan == 'c':
                taxon_name = "c_%s" %(row.loc[['c']].values[0])
            elif first_nonan == 'p':
                taxon_name = "p_%s" %(row.loc[['p']].values[0])
            elif first_nonan == 'k':
                taxon_name = "k_%s" %(row.loc[['k']].values[0])
            else:
                taxon_name = "None"

            return taxon_name

        #applying function to each row of the taxa key file
        taxon_key['taxa'] = taxon_key.apply(lambda x : taxon_condense(x), axis=1)

        #manual correction of names, these should be checked by looking at the ASV sequences and see how they match to the new name 
        taxon_key['taxa'] = taxon_key['taxa'].replace({'g_Gardnerella':'Gardnerella_vaginalis','Lactobacillus_acidophilus/casei/crispatus/gallinarum':'Lactobacillus_crispatus'
                                                        ,'Lactobacillus_fornicalis/jensenii':'Lactobacillus_jensenii','g_Escherichia/Shigella':'g_Escherichia.Shigella'
                                                        ,'Lactobacillus_gasseri/johnsonii':'Lactobacillus_gasseri'})

        #creating a dataframe for merging with just the information from the new condense column
        taxon_merge = taxon_key[['taxa']]
        #merging the counts table with the taxa table
        counts_table_named = pd.merge(left=taxon_merge,right=counts_table,right_index=True,left_index=True,how="inner")
        #grouping asvs with the same name and summing
        counts_table_named = counts_table_named.groupby('taxa').sum()
        #transposing to a table with samples are rows and counts as columns
        counts_table_named = counts_table_named.T

        #sorting the table by the study wide read count for each taxa
        counts_table_named = counts_table_named.reindex(counts_table_named.sum().sort_values(ascending=False).index, axis=1)
        #summing the read counts for each sample to be used by valencia in calculation of relative abundance
        counts_table_named['read_count'] = counts_table_named.sum(axis=1)
        #moving read count to first column
        read_count_column = counts_table_named.pop('read_count')
        counts_table_named.insert(0,'read_count',read_count_column)

        #output two files, one with the new condenses table and one that matches the condensed taxa name back to the original ASV
        # counts_table_named.to_csv("taxon_table_asv_merged.csv",sep=",",index_label="sampleID")
        # taxon_key.to_csv("asv_condensed_taxa_names.csv",sep=",")

        st.divider()

        st.subheader("Outputs")

        output1 = convert_df(counts_table_named, 'sampleID')

        st.dataframe(counts_table_named)
        csv1 = counts_table_named.to_csv(index='sampleID')
        b64 = base64.b64encode(csv1.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="taxon_table_asv_merged.csv">Download CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)



        output2 = convert_df(taxon_key, False)

        st.dataframe(taxon_key)
        csv2 = counts_table_named.to_csv(index='sampleID')
        b64 = base64.b64encode(csv2.encode()).decode()

        href = f'<a href="data:file/csv;base64,{b64}" download="asv_condensed_taxa_names.csv">Download CSV file</a>'
        st.markdown(href, unsafe_allow_html=True)
