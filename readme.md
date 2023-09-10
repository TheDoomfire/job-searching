# Job Searcher Arbestförmedlingen

För att söka jobb i arbetsförmedlingens hemsida


fieldset

## TODO

1. Read the json and take all needed info.
1. Take the URL and html_request and webscrape for referens and link
1. Save all this info to a csv file.

1. Opens up every URL

1. Take all the jobs in the .CSV
1. Opens up chromedriver (for selenium)
1. And if I press a specific button then: auto-aktivitetsrapportera


Auto-applying Idea
1. Search for errors/404
1. Search for any input fields. Except search. Need at least x amount of input fields.
1. If not, search for button/link with 


## Install Eveything

python -m pip install PACKAGENAME


## Basics

Create a venv `python -m venv .venv` //Name the folder whatever you want.

Activate it - Win: `source .venv/Scripts/activate` <!--  Mac: `source .venv/bin/activate` -->


### Requirements

`pip freeze > requirements.txt` - Create the requirements.txt
`pip install -r requirements.txt` - Installs it.


### Other

1. `playwright codegen` - for generating simple playwright script.


## Fixa dessa

1. Söker endast jobb från förra månaden 



not any(arbetsgivare in item.find("div")[5].text.lower() for arbetsgivare in skit_arbetsgivare)


<a _ngcontent-odm-c74="" rel="nofollow" role="button" target="_blank" class="d-print-none btn btn-primary" data-event-category="AS - Platsbanken" data-event-value="1" href="http://www.uniflex.se/jobbannons?jaid=59729" data-event-action="AS - Platsbanken - Annonssida - Ansök här - Btn - Click" data-event-name="AS - Platsbanken - Visat intresse på Annonssida">Ansök här</a>


## Ladda ner i en json file
https://data.jobtechdev.se/annonser/search-stats/index.html

*Perfect!!*
https://data.jobtechdev.se/annonser/jobtechlinks/index.html

Ladda ner "2022-07-31.tar.gz" filen, sedan få

## Job Searching

1. Playwright open the url
1. Get past the EU cookie thing
1. Get entire html in text format
1. Find forms

1. No form? Look for button "sök jobb" etc.
1. if found, playwright.click it.
1. Run the function again.

1. If form with atleast 2 input fields
1. And atleast 1 upload input

1. Read label for each input


## Shit Code:


			
<span class="wpcf7-form-control-wrap cf" data-name="your-first-name"><div class="mdc-text-field mdc-text-field--outlined cf7md-initialized"><input size="40" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required mdc-text-field__input" aria-required="true" aria-invalid="false" value="" type="text" name="your-first-name" required="required">
					
											<div class="mdc-notched-outline mdc-notched-outline--upgraded cf7md-initialized">
							<div class="mdc-notched-outline__leading"></div>
							<div class="mdc-notched-outline__notch">
								<label class="mdc-floating-label" for="your-first-name" style="">Förnamn</label>
							</div>
							<div class="mdc-notched-outline__trailing"></div>
						</div>
									</div></span>