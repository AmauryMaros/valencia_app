import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":house:",
)

st.sidebar.subheader("Contact")
st.sidebar.write("mfrance@som.umaryland.edu")

st.image("medias/valencia_Logo.png")

st.divider()

st.markdown('<div style="text-align: justify;"><b>VALENCIA</b> is a nearest-centroid based algorithm for the classification of human vaginal microbial community into \
            state types based on their taxonomic composition. Samples are individually assigned to community state types (CSTs) based on their similarity to a set \
            of thirteen reference centroids. The assignments provided by VALENCIA are reproducible and comparable across studies. Reference centroids were identified \
            and defined using a dataset of >13,000 vaginal microbial taxonomic compositions from >1,900 North American women. We have done fairly extensive work to validate\
             the usage of VALENCIA on vaginal microbial communities (see publication) including those that were derived from sequencing the V1V3, V3V4 and V4 regions.\
             We have also looked at how it performs on samples from adolescent girls and post menopausal women, as well as on reproductive age African women.</div>',
               unsafe_allow_html = True)

st.divider()

st.subheader("CST Architecture")

st.write("**CST I** communities are dominated by *L. crispatus* and include subtypes:")
st.write("- CST **I-A:** almost completely *L. crispatus*")
st.write("- CST **I-B:** less *L. crispatus* but still majority")

st.write("**CST II** communities are dominated by *L. gasseri*")

st.write("**CST III** communities are dominated by *L. iners* and include subtypes:")
st.write("- CST **III-A:** almost completely *L. iners*")
st.write("- CST **III-B:** less *L. iners* but still majority")

st.write("**CST IV** communities that have a low relative abundance of *Lactobacillus spp.* and include subtypes:")
st.write("- CST **IV-A:** contains a high to moderate relative abundance of *BVAB1* and *G. vaginalis*")
st.write("- CST **IV-B:** contains a high to moderate relative abundance of *G. vaginalis* and *A. vaginae*")
st.write("- CST **IV-C:** contains low relative abundances of *G. vaginalis*, *BVAB1*, and *Lactobacillus spp.* and includes:")
st.write("   - CST **IV-C0:** relatively even community with *Prevotella spp.*")
st.write("   - CST **IV-C1:** dominated by *Streptococcus spp.*")
st.write("   - CST **IV-C2:** dominated by *Enterococcus spp.*")
st.write("   - CST **IV-C3:** dominated by *Bifidobacterium spp.*")
st.write("   - CST **IV-C4:** dominated by *Staphylococcus spp.*")

st.write("**CST V** communities are dominated by *L. jensenii*")

st.divider()

st.subheader("Requirements")


st.markdown('<div style="text-align: justify;">\
            Taxa names need to match used by VALENCIA for proper CST assignment. We use species level assignments for the Lactobacillus, \
            Gardnerella, Prevotella, Atopobium and Sneathia. These appear as “Genus_species” format (e.g. “Lactobacillus_crispatus”. \
            All other taxa are summarized to the genus or higher level. These appear as “g_Genus” or “f_Family” (e.g. “g_Bifidobacterium”).\
             It is important that the major vaginal taxa’s names match the reference. This includes any critical in the definition of a CST,\
             which appear below. Prevotella often causes problems due variations in naming conventions. \
            If you are having difficulty with this taxa it is okay to combine all the data into "g_Prevotella",\
             just make sure to use the reference centroid with the matching change .</div>',unsafe_allow_html = True)