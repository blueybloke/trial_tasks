# Trial Tasks for PIT-M3D
This repo contains a couple of practice exercises for PITM3D.

## Task 1
Parse an [XML file](trial_tasks/tasks/tests/example.xml) and produce tokens.
```xml
<?xml version="1.0"?>
<metabolites>
  <metabolite>
    <creation_date>2005-11-16 15:48:42 UTC</creation_date>
    <update_date>2020-08-10 16:51:26 UTC</update_date>
    <accession>HMDB0000122</accession>
    <name>D-Glucose</name>
    <normal_concentrations>
      <concentration>
        <biospecimen>Blood</biospecimen>
        <concentration_value>3100-5600</concentration_value>
        <concentration_units>uM</concentration_units>
        <subject_age>Not Specified</subject_age>
        <subject_sex>Not Specified</subject_sex>
        <subject_condition>Normal</subject_condition>
        <references>
          <reference>
            <reference_text>Gibson KM, Burlingame TG, Hogema B, Jakobs C, Schutgens RB, Millington D, Roe CR, Roe DS, Sweetman L, Steiner RD, Linck L, Pohowalla P, Sacks M, Kiss D, Rinaldo P, Vockley J. 2-Methylbutyryl-coenzyme A dehydrogenase deficiency: a new inborn error of L-isoleucine metabolism. Pediatr Res. 2000 Jun;47(6):830-3.</reference_text>
            <pubmed_id>10832746</pubmed_id>
          </reference>
        </references>
      </concentration>
      <concentration>
        <biospecimen>Blood</biospecimen>
        <concentration_value>3890-5550</concentration_value>
        <concentration_units>uM</concentration_units>
        <subject_age>Not Specified</subject_age>
        <subject_sex>Not Specified</subject_sex>
        <subject_condition>Normal</subject_condition>
        <references>
          <reference>
            <reference_text>Conboy E, Vairo F, Schultz M, Agre K, Ridsdale R, Deyle D, Oglesbee D, Gavrilov D, Klee EW, Lanpher B. Mitochondrial 3-Hydroxy-3-Methylglutaryl-CoA Synthase Deficiency: Unique Presenting Laboratory Values and a Review of Biochemical and Clinical Features. JIMD Rep. 2018;40:63-69. doi: 10.1007/8904_2017_59</reference_text>
            <pubmed_id>29030856</pubmed_id>
          </reference>
        </references>
      </concentration>
    </normal_concentrations>
  </metabolite>
</metabolites>
```
Note: I have modified this XML file slightly from the one printed since there were some missing opening/closing tags.

## Task 2
Develop a backend for the given frontend.
