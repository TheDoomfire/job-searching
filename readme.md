# Job Searcher Arbestförmedlingen

För att söka jobb i arbetsförmedlingens hemsida


## TODO

1. Gå till URL för jobben.
1. Försök auto söka jobben. (med selenium)
1. Spara jobben jag sökt i en fil.

Download and unzips the json file. Then reads from it and save all jobs I may want in a csv file. Read from CSV file and go to webpages and apply for the jobs.

## Install Eveything

pip install -r requirements.txt

python -m pip install PACKAGENAME


## Fixa dessa

1. Söker endast jobb från förra månaden 



not any(arbetsgivare in item.find("div")[5].text.lower() for arbetsgivare in skit_arbetsgivare)


<a _ngcontent-odm-c74="" rel="nofollow" role="button" target="_blank" class="d-print-none btn btn-primary" data-event-category="AS - Platsbanken" data-event-value="1" href="http://www.uniflex.se/jobbannons?jaid=59729" data-event-action="AS - Platsbanken - Annonssida - Ansök här - Btn - Click" data-event-name="AS - Platsbanken - Visat intresse på Annonssida">Ansök här</a>


## Ladda ner i en json file
https://data.jobtechdev.se/annonser/search-stats/index.html

*Perfect!!*
https://data.jobtechdev.se/annonser/jobtechlinks/index.html

Ladda ner "2022-07-31.tar.gz" filen, sedan få


{"originalJobPosting":{"url":"https://arbetsformedlingen.se/platsbanken/annonser/26349350","hiringOrganization":{"name":"Brothers Team Bemanning AB","address":"Brothers Team Bemanning AB","url":null,"@context":"http://schema.org/","@type":"Organization"},"title":" C-Chaufför - 10 anställningar sökes (Heltid)","employmentType":"Vanlig anställning","relevantOccupation":{"@type":"Occupation","@context":"http://schema.org/","occupationalCategory":{"codeValue":"JEhg_Dmh_mzv","@type":"CategoryCode","@context":"http://schema.org/"},"name":"Distributionsförare"},"totalJobOpenings":10,"@type":"JobPosting","scraper":"arbetsformedlingen.se","identifier":"26349350","jobLocation":{"addressLocality":"Vällingby","streetAddress":"Ryttmästarvägen 174","postalCode":"16270","@type":"PostalAddress","@context":"http://schema.org/"},"experienceRequirements":"","@context":"http://schema.org/","validThrough":"2022-08-24","datePosted":"2022-07-24"},"firstSeen":"2022-07-25T00:48:56","id":"6e6b226b8e7092ef0989491b06eb4b4e","detected_language":"sv","application_deadline":"2022-08-24T23:59:59","text_enrichments_results":{"enriched_result":{"enriched_candidates":{"occupations":[{"concept_label":"C-chaufför","term":"c-chaufför","term_misspelled":false,"prediction":0.568642288},{"concept_label":"Chaufför","term":"chaufförer","term_misspelled":false,"prediction":0.9211942852}],"competencies":[{"concept_label":"C-körkort","term":"c-körkort","term_misspelled":false,"prediction":0.26444304},{"concept_label":"Ykb","term":"ykb","term_misspelled":false,"prediction":0.389277816},{"concept_label":"Förarkort","term":"förarkort","term_misspelled":false,"prediction":0.384460151},{"concept_label":"Lastning","term":"lastning","term_misspelled":false,"prediction":0.560338944},{"concept_label":"Lossning","term":"lossning","term_misspelled":false,"prediction":0.574828982},{"concept_label":"Distribution","term":"distribution","term_misspelled":false,"prediction":0.702268302},{"concept_label":"Pallar","term":"pallar","term_misspelled":false,"prediction":0.595148683}],"traits":[],"geos":[{"concept_label":"Stockholm","term":"stockholm","term_misspelled":false,"prediction":0.0258860588}]}},"enrichedbinary_result":{"enriched_candidates":{"occupations":[{"concept_label":"Chaufför","term":"chaufförer","term_misspelled":false},{"concept_label":"C-chaufför","term":"c-chaufför","term_misspelled":false}],"competencies":[{"concept_label":"Lastning","term":"lastning","term_misspelled":false},{"concept_label":"Lossning","term":"lossning","term_misspelled":false},{"concept_label":"Pallar","term":"pallar","term_misspelled":false},{"concept_label":"Distribution","term":"distribution","term_misspelled":false}],"traits":[],"geos":[]}}},"workplace_addresses":[],"ssyk_lvl4":8332,"hashsum":"A8KHVGw=AsKLczY=CsKwbsKGA3wFTABF9BYwBXRpfQAGrCscKICcKFwqMZ+94c236afd0619a9c2f6f87a0aaa02b01","sourceLinks":[{"displayName":"arbetsformedlingen.se","link":"https://arbetsformedlingen.se/platsbanken/annonser/26349350"}],"isValid":true,"brief_description":"Vi på Brothers Team Bemanning AB söker för tillfället 10 heltidsanställda chaufförer med C-körkort, YKB och förarkort. Vi erbjuder dig en trygg anställning på en väldigt attraktiv arbetsplats, med en marknadsenlig chaufförslön samt ob-ersättning, enligt avtal.","date_to_display_as_publish_date":"2022-07-24T00:00:00","original_source_links":[{"displayName":"arbetsformedlingen.se","link":"https://arbetsformedlingen.se/platsbanken/annonser/26349350"}]}


"addressLocality":"Örebro"
"firstSeen":"2022-01-01" - Get maybe last months
"title":
"name":
Get "url"

Download link:

{"originalJobPosting":{"@type":"JobPosting","totalJobOpenings":3,"relevantOccupation":{"occupationalCategory":{"codeValue":"heGV_uHh_o8W","@context":"http://schema.org/","@type":"CategoryCode"},"name":"Arbetsterapeut","@type":"Occupation","@context":"http://schema.org/"},"identifier":"26167569","scraper":"arbetsformedlingen.se","url":"https://arbetsformedlingen.se/platsbanken/annonser/26167569","hiringOrganization":{"@type":"Organization","url":"http://www.mabrahalsa.se","@context":"http://schema.org/","name":"Må Bra Hälsa i Danderyd AB","address":"MåBra Hälsa Hammarby Sjöstad"},"title":"  Arbetsterapeut konsult eller anställd  MåBra Hälsa AB Primärvård","employmentType":"Vanlig anställning","@context":"http://schema.org/","datePosted":"2022-06-02","validThrough":"2022-08-20","jobLocation":{"postalCode":"12030","@type":"PostalAddress","@context":"http://schema.org/","addressLocality":"Stockholm","streetAddress":"Virkesvägen 6"},"experienceRequirements":"Arbetsterapeut - Erfarenhet efterfrågas"},"id":"0657f38a4f87a21b3b3edb8e9a94497a","firstSeen":"2022-06-03T00:55:16","detected_language":"sv","application_deadline":"2022-08-20T23:59:59","text_enrichments_results":{"enriched_result":{"enriched_candidates":{"occupations":[{"concept_label":"Arbetsterapeut","term":"arbetsterapeut","term_misspelled":false,"prediction":0.630943656}],"competencies":[{"concept_label":"Hälsa","term":"hälsa","term_misspelled":false,"prediction":0.094073772},{"concept_label":"Primärvård","term":"primärvård","term_misspelled":false,"prediction":0.03616035},{"concept_label":"Sjukvård","term":"vård","term_misspelled":false,"prediction":0.053651631},{"concept_label":"Friskvård","term":"friskvård","term_misspelled":false,"prediction":0.137064934},{"concept_label":"Vision","term":"vision","term_misspelled":false,"prediction":0.027612805},{"concept_label":"Friskvård","term":"friskvård","term_misspelled":false,"prediction":0.006487906},{"concept_label":"Sjukvård","term":"vård","term_misspelled":false,"prediction":0.007484436},{"concept_label":"Sjukvård","term":"vård","term_misspelled":false,"prediction":0.428660154},{"concept_label":"Hälsa","term":"hälsa","term_misspelled":false,"prediction":0.443293929},{"concept_label":"Kost","term":"kost","term_misspelled":false,"prediction":0.339191318},{"concept_label":"Sjukvård","term":"vård","term_misspelled":false,"prediction":0.377475917},{"concept_label":"Ergonomi","term":"ergonomi","term_misspelled":false,"prediction":0.07197082},{"concept_label":"Hälsa","term":"hälsa","term_misspelled":false,"prediction":0.012584448},{"concept_label":"Arbetsterapi","term":"arbetsterapi","term_misspelled":false,"prediction":0.638242662},{"concept_label":"Tilläggsarbeten","term":"tilläggsarbete","term_misspelled":false,"prediction":0.19788456}],"traits":[{"concept_label":"Arbeta självständigt","term":"arbeta självständigt","term_misspelled":false,"prediction":0.805527449},{"concept_label":"Arbeta självständigt","term":"arbeta självständigt","term_misspelled":false,"prediction":0.106097162}],"geos":[{"concept_label":"Stockholm","term":"stockholm","term_misspelled":false,"prediction":0.0459084809},{"concept_label":"Danderyd","term":"danderyd","term_misspelled":false,"prediction":0.0450230837},{"concept_label":"Mörby centrum","term":"mörby centrum","term_misspelled":false,"prediction":0.015752852},{"concept_label":"Hammarby sjöstad","term":"hammarby sjöstad","term_misspelled":false,"prediction":0.0231672525},{"concept_label":"Nacka","term":"nacka","term_misspelled":false,"prediction":0.07786569},{"concept_label":"Nacka","term":"nacka","term_misspelled":false,"prediction":0.0188489556},{"concept_label":"Danderyd","term":"danderyd","term_misspelled":false,"prediction":0.0095978379}]}},"enrichedbinary_result":{"enriched_candidates":{"occupations":[{"concept_label":"Arbetsterapeut","term":"arbetsterapeut","term_misspelled":false}],"competencies":[{"concept_label":"Arbetsterapi","term":"arbetsterapi","term_misspelled":false}],"traits":[{"concept_label":"Arbeta självständigt","term":"arbeta självständigt","term_misspelled":false}],"geos":[]}}},"workplace_addresses":[],"ssyk_lvl4":2330,"hashsum":"AVlrGgAS8gQwAsOiA8KdBG01NABBTDtcK5AXTDiMOoADnChXc=AFF3wpw=+81275d86ff7f0d42cfe3b43731b6ccc2","sourceLinks":[{"displayName":"arbetsformedlingen.se","link":"https://arbetsformedlingen.se/platsbanken/annonser/26167569"}],"isValid":true,"brief_description":"VI SÖKER MEDARBETARE TILL SAMTLIGA MOTTAGNINGARVi är ett Hälsocentrum som bedrivit vård med vårdavtal och friskvård i snart 20 år. Idag finns vi på fyra ställen i Stockholm.","date_to_display_as_publish_date":"2022-06-02T00:00:00","original_source_links":[{"displayName":"arbetsformedlingen.se","link":"https://arbetsformedlingen.se/platsbanken/annonser/26167569"}]}



/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-job/div/section/div/div[2]/div[2]/aside[1]/div/pb-section-job-apply-component/div/div/div[2]

//*[@id="pb-root"]/pb-page-job/div/section/div/div[2]/div[2]/aside[1]/div/pb-section-job-apply-component/div/div/div[2]


/html/body/div[1]/div[2]/div[8]/div/div/main/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[2]/pb-root/div/pb-page-job/div/section/div/div[2]/div[2]/aside[1]/div/pb-section-job-apply-component/div/div/div[2]/strong

//*[@id="pb-root"]/pb-page-job/div/section/div/div[2]/div[2]/aside[1]/div/pb-section-job-apply-component/div/div/div[2]/strong