# Raw header and footer code copied from GC websites. This html is injected into the webapp using dash-dangerously-set-inner-html

from .config import Config
from flask_babel import _ ,Babel
app_config = Config()

app_title_en = '''
  <div id="header" role='region' aria-label="title" class="container" style="margin-bottom: 25px;">
    <div class='flex-display justify-space-between'>
      <div class="">
      <!-- 
        <img id="csa-image" alt="CSA Logo" src="/scisat/assets/csa-logo.png" style="height: 60px; width: auto; margin: 25px;">
      -->
      </div>
      <div id="title" class="">
        <h1 id="page-title" >'''+_('Alouette I ionogram data') +'''</h1>
      </div>
      <div id="button-div" style="display: flex; align-items: center;" >
        <a id="learn-more-link" href="https://www.asc-csa.gc.ca/eng/satellites/scisat/about.asp" class="btn btn-primary">
          <span id="learn-more-button">'''+_('Learn more about Alouette') +'''</span>
        </a>
      </div>
    </div>
  </div>
'''

app_title_fr = '''
  <div id="header" role='region' aria-label="titre" class="container" style="margin-bottom: 25px;">
    <div class='flex-display justify-space-between'>
      <div class="">
      <!-- 
        <img id="csa-image" alt="CSA Logo" src="/scisat/assets/csa-logo.png" style="height: 60px; width: auto; margin: 25px;">
      -->
      </div>
      <div id="title" class="">
        <h1 id="page-title" >Données d'ionogrammes de l'Alouette I</h1>
      </div>
      <div id="button-div" style="display: flex; align-items: center;" >
        <a id="learn-more-link" href="https://www.asc-csa.gc.ca/eng/satellites/scisat/about.asp" class="btn btn-primary">
          <span id="learn-more-button">En apprendre plus sur Alouette</span>
        </a>
      </div>
    </div>
  </div>
'''

gc_breadcrumb_en = '''
<nav id="wb-bc" aria-label="breadcrumb" property="breadcrumb">
    <h2>You are here:</h2>
    <div class="container">
      <ol class="breadcrumb">
        <li><a href="https://www.canada.ca/en.html">Canada.ca</a></li>
        <li><a href="https://www.asc-csa.gc.ca/eng/default.asp">Canadian Space Agency</a></li>
      </ol>
    </div>
</nav>
'''

gc_breadcrumb_fr = '''
<nav id="wb-bc"  aria-label="Fil d'ariane" property="breadcrumb">
    <h2>Vous êtes ici :</h2>
    <div class="container">
      <ol class="breadcrumb">
        <li><a href="https://www.canada.ca/fr.html">Canada.ca</a></li>
        <li><a href="https://www.asc-csa.gc.ca/fra/default.asp">Agence spatiale canadienne</a></li>
      </ol>
    </div>
</nav>
'''

gc_menu_items_en='''
<li role="presentation">
  <a role="menuitem" tabindex="0" aria-haspopup="true" aria-controls="gc-mnu-jobs" aria-expanded="false" href="#">Jobs and the workplace</a>
  <ul id="gc-mnu-jobs" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/jobs.html">Jobs<span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/jobs/opportunities.html">Find a job</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/jobs/training.html">Training</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/business-management">Hiring and managing employees</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/start-business">Starting a business</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/jobs/workplace.html">Workplace standards</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/pensions.html">Pensions and retirement</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/ei.html">Employment Insurance benefits and leave</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-jobs-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-jobs-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/employment-social-development/programs/ei/ei-list/ei-roe/access-roe.html">View your Records of Employment</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/employment-social-development/services/sin.html">Apply for a Social Insurance Number (SIN)</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/employment-social-development/services/foreign-workers.html">Hire a temporary foreign worker</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry.html">Immigrate as a skilled worker</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-cit" aria-expanded="false" href="#">Immigration and citizenship</a>
  <ul id="gc-mnu-cit" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/immigration-citizenship.html">Immigration<span class="hidden-xs hidden-sm"> and citizenship</span><span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/application.html">My application</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/visit-canada.html">Visit</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada.html">Immigrate</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada.html">Work</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada.html">Study</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-citizenship.html">Citizenship</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/new-immigrants.html">New immigrants</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/canadians.html">Canadians</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/refugees.html">Refugees and asylum</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/immigration-citizenship/enforcement-violations.html">Enforcement and violations</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-cit-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-cit-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/application/account.html">Sign in or create an account to apply online</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-status.html">Check your application status</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/application/check-processing-times.html">Check application processing times</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/application/application-forms-guides.html">Find an application form</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cic.gc.ca/english/information/fees/index.asp">Pay your fees</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cic.gc.ca/english/visit/visas.asp">Find out if you need an eTA or a visa to visit Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cic.gc.ca/english/helpcentre/index-featured-can.asp">Have questions? Find answers in the Help Centre</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-travel" aria-expanded="false" href="#">Travel and tourism</a>
  <ul id="gc-mnu-travel" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://travel.gc.ca/">Travel<span class="hidden-xs hidden-sm"> and tourism</span><span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/travelling/advisories">Travel advice and advisories</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/travel-covid">COVID-19: Travel, quarantine and borders</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/visit">Visit Canada</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/travelling">Travel abroad</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/air">Air travel</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/returning">Return to Canada</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/immigration-refugees-citizenship/services/canadian-passports.html">Canadian passports</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/canadian-tourism">Canadian attractions, events and experiences</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/assistance/ask-travel">Ask travel</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/assistance">Assistance abroad</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/stay-connected">Stay connected</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-travel-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-travel-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/travelling/children/consent-letter">Consent letter for children travelling abroad</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cbsa-asfc.gc.ca/bwt-taf/menu-eng.html">Canada - U.S. border wait times</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/travelling/registration">Register as a Canadian abroad</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cbsa-asfc.gc.ca/prog/nexus/application-demande-eng.html">Apply for NEXUS</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/returning/customs/what-you-can-bring-home-to-canada">What you can bring home to Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/assistance/embassies-consulates">Contact an embassy or consulate</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/travelling/cannabis-and-international-travel">Cannabis and international travel</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-biz" aria-expanded="false" href="#">Business and industry</a>
  <ul id="gc-mnu-biz" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business.html">Business<span class="hidden-xs hidden-sm"> and industry</span><span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/start.html">Starting a business</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/grants.html">Business grants and financing</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/taxes.html">Business taxes</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/federal-corporations.html">Federal corporations</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/hire.html">Hiring and managing employees</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/trade.html">International trade and investment</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/permits.html">Permits, licences and regulations</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/doing-business.html">Doing business with government</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science/innovation.html">R&amp;D and innovation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/research.html">Research and business intelligence</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/ip.html">Intellectual property and copyright</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/maintaingrowimprovebusiness.html">Maintaining your business</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/protecting.html">Protecting your business</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/bankruptcy.html">Insolvency for business</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-biz-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-biz-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/fdrlCrpSrch.html?locale=en_CA">Find a corporation</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.cbsa-asfc.gc.ca/prog/manif/portal-portail-eng.html">Report your imported goods</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.ic.gc.ca/app/opic-cipo/trdmrks/srch/home?lang=eng">Search for trademarks</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/2018/html/tblmod-1-eng.html">Review custom tariffs for importing goods</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.ic.gc.ca/opic-cipo/cpd/eng/introduction.html">Find a patent</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.cbsa-asfc.gc.ca/comm-eng.html">Import and export from Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://ic.gc.ca/eic/site/cd-dgc.nsf/eng/h_cs03922.html">Name a business</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/hm.html?locale=en_CA">Make changes to your corporation (Online Filing Centre)</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-benny" aria-expanded="false" href="#">Benefits</a>
  <ul id="gc-mnu-benny" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits.html">Benefits<span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.canada.ca/en/services/benefits/covid19-emergency-benefits.html">COVID-19 – Benefits and services </a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/ei.html">Employment Insurance benefits and leave</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/family.html">Family and caregiving benefits</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/publicpensions.html">Public pensions</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/education.html">Student aid and education planning</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/housing.html">Housing benefits</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/disability.html">Disability benefits</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.canada.ca/en/services/benefits/audience.html">Benefits by audience</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/calendar.html">Benefits payment dates</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://benefitsfinder.services.gc.ca/hm?GoCTemplateCulture=en-CA">Benefits finder</a></li>

    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-benny-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-benny-sub" role="menu" aria-orientation="vertical">

        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/ei/ei-regular-benefit.html">Apply for Employment Insurance</a></li>

       <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/education/student-aid/grants-loans.html">Apply for student loans and grants</a></li>
       <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/government/sign-in-online-account.html">Sign in to a Government of Canada online account</a></li>

        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.tpsgc-pwgsc.gc.ca/recgen/txt/depot-deposit-eng.html">Sign up for direct deposit</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/benefits/ei/ei-internet-reporting.html">Submit your EI report</a></li>

        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cra-arc.gc.ca/bnfts/clcltr/cfbc-eng.html">Child and family benefits calculators</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-health" aria-expanded="true" href="#">Health</a>
  <ul id="gc-mnu-health" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health.html">Health<span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health/food-nutrition.html">Food and nutrition</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/public-health/services/diseases.html">Diseases and conditions</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/public-health/topics/immunization-vaccines.html">Vaccines and immunization</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health/drug-health-products.html">Drug and health products</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health/product-safety.html">Product safety</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health/health-risks-safety.html">Health risks and safety</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health/healthy-living.html">Healthy living</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health/aboriginal-health.html">Indigenous health</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health/health-system-services.html">Health system and services</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/health/science-research-data.html">Science, research and data</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-health-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-health-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/health-canada/services/drugs-medication/cannabis/industry-licensees-applicants/licensed-cultivators-processors-sellers.html">Licensed cultivators, processors and seller of cannabis</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://healthycanadians.gc.ca/recall-alert-rappel-avis/index-eng.php">Food and product recalls and safety alerts</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/health-canada/services/canada-food-guides.html">Canada's food guide</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-taxes" aria-expanded="false" href="#">Taxes</a>
  <ul id="gc-mnu-taxes" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/taxes.html">Taxes<span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/taxes/income-tax.html">Income tax</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses.html">GST/HST</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/payroll.html">Payroll</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/taxes/business-number.html">Business number</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/taxes/savings-and-pension-plans.html">Savings and pension plans</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/taxes/child-and-family-benefits.html">Child and family benefits</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/taxes/excise-taxes-duties-and-levies.html">Excise taxes, duties, and levies</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/taxes/charities.html">Charities and giving</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-taxes-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-taxes-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/e-services/e-services-individuals/account-individuals.html">My Account</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/e-services/e-services-businesses/business-account.html">My Business Account</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/e-services/represent-a-client.html">Represent a Client</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/e-services/e-services-businesses/gst-hst-netfile.html">File a GST/HST return (NETFILE)</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/make-a-payment-canada-revenue-agency.html">Make a payment to the Canada Revenue Agency</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/child-family-benefits/benefit-payment-dates.html">Find the next benefit payment date</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-enviro" aria-expanded="false" href="#">Environment and natural resources</a>
  <ul id="gc-mnu-enviro" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/environment.html">Environment<span class="hidden-xs hidden-sm"> and natural resources</span><span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/environment/weather.html">Weather, climate and hazards</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/environment/energy.html">Energy</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/environment/natural-resources.html">Natural resources</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.agr.gc.ca/eng/agriculture-and-the-environment/?id=1580153237101">Agriculture and the environment</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/environment/fisheries.html">Fisheries</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/environment/wildlife-plants-species.html">Wildlife, plants and species</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/environment/pollution-waste-management.html">Pollution and waste management</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/environment/conservation.html">Environmental conservation and protection</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-enviro-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-enviro-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://weather.gc.ca/canada_e.html">Local weather forecast</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrcan.gc.ca/energy/efficiency/transportation/20996">Fuel-efficient vehicles</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrcan.gc.ca/homes">Home energy efficiency</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/environment-climate-change/services/species-risk-public-registry.html">Species at risk</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/environment-climate-change/services/seasonal-weather-hazards.html">Prepare for severe weather</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-defence" aria-expanded="false" href="#">National security and defence</a>
  <ul id="gc-mnu-defence" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/defence.html"><span class="hidden-xs hidden-sm">National security and defence</span><span class="visible-xs-inline visible-sm-inline">Defence: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/defence/nationalsecurity.html">National security</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/defence/caf.html">Canadian Armed Forces</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/defence/defence-equipment-purchases-upgrades.html">Defence equipment purchases and upgrades</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/transportation-security.html">Transportation security</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/defence/securingborder.html">Securing the border</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/defence/cybersecurity.html">Cyber security</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/defence/jobs.html">Jobs in national security and defence</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/government/publicservice/benefitsmilitary.html">Services and benefits for the military</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-defence-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-defence-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://forces.ca/en/careers/">Jobs in the Canadian Armed Forces</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/department-national-defence/services/military-history/history-heritage/insignia-flags/ranks/rank-appointment-insignia.html">Military ranks</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/defence/caf/equipment.html">Defence equipment</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.publicsafety.gc.ca/cnt/ntnl-scrt/cntr-trrrsm/lstd-ntts/crrnt-lstd-ntts-en.aspx">Current list of terrorist entities</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cadets.ca/en/join/cadets.page">Join the Cadets</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://dgpaapp.forces.gc.ca/en/canada-defence-policy/index.asp">Canada's Defence policy</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-culture" aria-expanded="false" href="#">Culture, history and sport</a>
  <ul id="gc-mnu-culture" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture.html">Culture<span class="hidden-xs hidden-sm">, history and sport</span><span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/canadian-heritage/services/funding.html">Funding - Culture, history and sport</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/events-celebrations-commemorations.html">Events, celebrations and commemorations</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/cultural-attractions.html">Cultural landmarks and attractions</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/canadian-identity-society.html">Canadian identity and society</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/sport.html">Sport</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/history-heritage.html">History and heritage</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/arts-media.html">Arts and media</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/cultural-youth-programs.html">Cultural youth programs</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/cultural-trade-investment.html">Cultural trade and investment</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-culture-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-culture-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.veterans.gc.ca/eng/remembrance/memorials/canadian-virtual-war-memorial">Visit the Canadian Virtual War Memorial</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/canadian-identity-society/anthems-symbols.html">Anthems and symbols of Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://crtc.gc.ca/eng/8045/d2018.htm">Find a CRTC decision</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.bac-lac.gc.ca/eng/search/Pages/ancestors-search.aspx">Research your family history</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.bac-lac.gc.ca/eng/census/Pages/census.aspx">Search census records</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/culture/cultural-attractions/attractions-canada-capital.html">Landmarks and attractions in Canada's capital</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-policing" aria-expanded="false" href="#">Policing, justice and emergencies</a>
  <ul id="gc-mnu-policing" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing.html">Policing<span class="hidden-xs hidden-sm">, justice and emergencies</span><span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing/police/index.html">Policing</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing/justice.html">Justice</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing/emergencies.html">Emergencies</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing/corrections.html">Corrections</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing/parole.html">Parole, record suspension, expungement and clemency</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing/victims.html">Victims of crime</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-policing-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-policing-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.rcmp-grc.gc.ca/cfp-pcaf/online_en-ligne/index-eng.htm">Apply/Renew a firearms licence</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.rcmp-grc.gc.ca/en/criminal-record-checks">Get a criminal records check</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/parole-board/services/record-suspensions/official-pbc-application-guide-and-forms.html">Apply for a criminal record suspension</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.getprepared.gc.ca/cnt/hzd/drng-en.aspx">What to do during an emergency</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing/police/community-safety-policing/impaired-driving.html">Know the law on impaired driving</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/policing/police/help-solve-crime.html">Help solve a crime</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-trans" aria-expanded="false" href="#">Transport and infrastructure</a>
  <ul id="gc-mnu-trans" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/transport.html">Transport<span class="hidden-xs hidden-sm"> and infrastructure</span><span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/aviation.html">Aviation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/marine.html">Marine transportation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/road.html">Road transportation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/rail.html">Rail transportation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/dangerous-goods.html">Dangerous goods</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/infrastructure.html">Infrastructure</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-trans-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-trans-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/aviation/drone-safety.html">Drone safety</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://tc.canada.ca/en/aviation/aviation-security/what-not-bring-plane">What you can't bring on an airplane</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/eng/marinesafety/oep-vesselreg-menu-728.htm">Register your vessel</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/en/services/road/child-car-seat-safety.html">Child car seat safety</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/eng/tdg/clear-tofc-211.htm">Transporting dangerous goods - Regulations</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/eng/acts-regulations/regulations-sor96-433.htm">Canadian Aviation Regulations</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-canworld" aria-expanded="false" href="#">Canada and the world</a>
  <ul id="gc-mnu-canworld" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/index.aspx?lang=eng">Canada and the world<span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/offices-bureaux/index.aspx?lang=eng">International offices and emergency contacts</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/study_work_travel-etude_travail_voyage/index.aspx?lang=eng">Study, work and travel worldwide</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/country-pays/index.aspx?lang=eng">Information by countries and territories</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://international.gc.ca/world-monde/stories-histoires/index.aspx?lang=eng">Stories</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/international_relations-relations_internationales/index.aspx?lang=eng">International relations</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/issues_development-enjeux_developpement/index.aspx?lang=eng">Global issues and international assistance</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/funding-financement/index.aspx?lang=eng">Funding for international initiatives</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.canada.ca/en/services/business/trade/index.html">International trade and investment</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-canworld-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-canworld-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.international.gc.ca/world-monde/covid-19/index.aspx?lang=eng">COVID-19: Trade, foreign affairs, international trade and development</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://scholarships-bourses.gc.ca/scholarships-bourses/non_can/opportunities-opportunites.aspx?lang=eng">Find a Canadian scholarship as an international student</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://treaty-accord.gc.ca/index.aspx">International treaties signed by Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://educanada.ca/index.aspx?lang=eng">Find international study or research opportunities in Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://travel.gc.ca/assistance/embassies-consulates">Contact an embassy or consulate</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/protocol-protocole/reps.aspx?lang=eng">Contact a foreign representative in Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.international.gc.ca/gac-amc/about-a_propos/services/authentication-authentification/step-etape-1.aspx?lang=eng">Authenticate a document</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-money" aria-expanded="false" href="#">Money and finances</a>
  <ul id="gc-mnu-money" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance.html"><span class="hidden-xs hidden-sm">Money and finances</span><span class="visible-xs-inline visible-sm-inline">Finance: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/manage.html">Managing your money</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/debt.html">Debt and borrowing</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/savings.html">Savings and investments</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/educationfunding.html">Education funding</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/pensions.html">Pensions and retirement</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/fraud.html">Protection from frauds and scams</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/tools.html">Financial tools and calculators</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/financial-consumer-agency/services/financial-literacy-programs.html">Financial literacy programs</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/consumer-affairs.html">Consumer affairs</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/finance/bankruptcy.html">Insolvency</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/taxes.html">Taxes</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/government/system/finances.html">Government finances</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/grants.html">Business grants and financing</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/permits/federallyregulatedindustrysectors/financialservicesregulation.html">Financial and money services regulation</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-money-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-money-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.ic.gc.ca/app/scr/bsf-osb/ins/login.html?lang=eng">Find a bankruptcy or insolvency record</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/jobs/education/student-financial-aid/student-loan.html">Student loans</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.tpsgc-pwgsc.gc.ca/recgen/txt/depot-deposit-eng.html">Set up direct deposit</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/financial-consumer-agency/services/mortgages.html">Mortgages</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/financial-consumer-agency/services/credit-reports-score.html">Credit report and scores</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://itools-ioutils.fcac-acfc.gc.ca/BC-CB/NetInc-RevNet-eng.aspx">Make a budget</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/revenue-agency/services/tax/registered-plans-administrators/pspa/mp-rrsp-dpsp-tfsa-limits-ympe.html">Rates and contribution limits</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-science" aria-expanded="false" href="#">Science and innovation</a>
  <ul id="gc-mnu-science" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science.html">Science<span class="hidden-xs hidden-sm"> and innovation</span><span class="visible-xs-inline visible-sm-inline">: home</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science/researchfunding.html">Research funding and awards</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science/sciencesubjects.html">Science subjects</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science/open-data.html">Open data, statistics and archives</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science/institutes.html">Research institutes and facilities</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science/innovation.html">R&amp;D and innovation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/business/ip.html">Intellectual property and copyright</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science/scientistsdirectory.html">Directory of scientists and research professionals</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/en/services/science/educationalresources.html">Science education resources</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-science-sub" aria-expanded="true">Most requested</a>
      <ul id="gc-mnu-science-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrc-cnrc.gc.ca/eng/publications/codes_centre/2015_national_building_code.html">National building codes</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrc-cnrc.gc.ca/eng/services/time/web_clock.html#tzpanel-4">Official time across Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrc-cnrc.gc.ca/eng/services/sunrise/index.html">Check sunrise and sunset times</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrc-cnrc.gc.ca/eng/irap/services/financial_assistance.html">Grants for technological innovation (IRAP)</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://science-libraries.canada.ca/eng/home/">Federal Science Library</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://asc-csa.gc.ca/eng/astronomy/auroramax/hd-480.asp">Live view of northern lights cam</a></li>
      </ul>
    </li>
  </ul>
</li>
'''

gc_header_en = '''
<div class='global-header'>
<nav aria-label='accessible menu' >
  <ul id="wb-tphp" class="wb-init wb-disable-inited">
	  <li class="wb-slc"><a class="wb-sl" href="#react-entry-point">Skip to main content</a></li>
	  <!-- <li class="wb-slc"><a class="wb-sl" href="#wb-info">Skip to "About government"</a></li>
    <li class="wb-slc"><a class="wb-sl" href="?wbdisable=true" rel="alternate">Switch to basic HTML version</a></li> -->
  </ul>
</nav>
<header aria-label='Page Header'>
	<div id="wb-bnr" class="container">
		<div class="row">
			<section id="wb-lng" class="col-xs-3 col-sm-12 pull-right text-right">
        <h2 class="wb-inv">Language selection</h2>
        <div class="row">
            <div class="col-md-12">
                <ul class="list-inline mrgn-bttm-0">
                    <li>
                        <a lang="fr" href="'''+ app_config.FR_LINK +'''">
                          <span class="hidden-xs">Français</span>
                          <abbr title="Français" class="visible-xs h3 mrgn-tp-sm mrgn-bttm-0 text-uppercase">fr</abbr>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
      </section>
				<div class="brand col-xs-9 col-sm-5 col-md-4" property="publisher" resource="#wb-publisher" typeof="GovernmentOrganization">
						<link href="https://canada.ca/content/canadasite/en.html" property="url">
							<img src="https://canada.ca/etc/designs/canada/wet-boew/assets/sig-blk-en.svg" alt="Government of Canada" property="logo">
							<span class="wb-inv"> /
								<span lang="fr">Gouvernement du Canada</span>
							</span>
					<meta property="name" content="Government of Canada">
					<meta property="areaServed" typeof="Country" content="Canada">
					<link property="logo" href="https://canada.ca/etc/designs/canada/wet-boew/assets/wmms-blk.svg">
				</div>
				<section id="wb-srch" class="col-lg-offset-4 col-md-offset-4 col-sm-offset-2 col-xs-12 col-sm-5 col-md-4">
					<h2>Search</h2>
          <form action="https://www.canada.ca/en/sr/srb.html" method="get" name="cse-search-box" role="search">
            <div class="form-group wb-srch-qry">
              <label for="wb-srch-q" class="wb-inv">Search Canada.ca</label>
              <input name="cdn" value="canada" type="hidden">
              <input name="st" value="s" type="hidden">
              <input name="num" value="10" type="hidden">
              <input name="langs" value="en" type="hidden">
              <input name="st1rt" value="1" type="hidden">
              <input name="s5bm3ts21rch" value="x" type="hidden">
                <input id="wb-srch-q" list="wb-srch-q-ac" class="wb-srch-q form-control" name="q" type="search" value="" size="34" maxlength="170" placeholder="Search Canada.ca">
              <input type="hidden" name="_charset_" value="UTF-8">
              <datalist id="wb-srch-q-ac">
              </datalist>
            </div>
            <div class="form-group submit">
            <button type="submit" id="wb-srch-sub" class="btn btn-primary btn-small" name="wb-srch-sub"><span class="glyphicon-search glyphicon"></span><span class="wb-inv">Search</span></button>
            </div>
          </form>
				</section>
		</div>
	</div>
	<nav class="gcweb-v2 gcweb-menu wb-init gcweb-menu-inited" aria-label="Main Navigation" typeof="SiteNavigationElement" id="wb-auto-2"><div class="container">
		<h2 class="wb-inv">Menu</h2>
		<button type="button" aria-haspopup="true" aria-expanded="false" aria-label="Press the SPACEBAR to expand or the escape key to collapse this menu. Use the Up and Down arrow keys to choose a submenu item. Press the Enter or Right arrow key to expand it, or the Left arrow or Escape key to collapse it. Use the Up and Down arrow keys to choose an item on that level and the Enter key to access it."><span class="wb-inv">Main </span>Menu <span class="expicon glyphicon glyphicon-chevron-down"></span></button>
		<ul role="menu" aria-orientation="vertical" data-ajax-replace="/content/dam/canada/sitemenu/sitemenu-v2-en.html" class="wb-init wb-data-ajax-replace-inited" id="wb-auto-3">
    '''+ gc_menu_items_en +'''
    </ul>
	</div></nav>
  '''+ gc_breadcrumb_en +'''

</header>
</div>
'''

gc_header_en_old ='''
<header>
    <div id="wb-bnr" class="container">
      <div class="row">
        <section id="wb-lng" class="col-xs-3 col-sm-12 pull-right text-right">
          <h2 class="wb-inv">Language selection</h2>
          <ul class="list-inline mrgn-bttm-0">
            <li>
              <a lang="fr" hreflang="fr" href="'''+ app_config.FR_LINK +'''">
              <span class="hidden-xs">Français</span>
              <abbr title="Français" class="visible-xs h3 mrgn-tp-sm mrgn-bttm-0 text-uppercase">fr</abbr>
              </a>
            </li>
          </ul>
        </section>
        <div class="brand col-xs-9 col-sm-5 col-md-4" property="publisher" typeof="GovernmentOrganization">
          <a href="https://www.canada.ca/en.html" property="URL">
            <img src="assets/gc_theme_cdn/assets/sig-blk-en.svg" alt="Government of Canada" property="logo">
              <span class="wb-inv"> /
                <span lang="fr">Gouvernement du Canada</span>
              </span></a>
          <meta property="name" content="Government of Canada">
          <meta property="areaServed" typeof="Country" content="Canada">
          <link property="logo" href="assets/gc_theme_cdn/assets/sig-blk-en.svg">
        </div>
        <section id="wb-srch" class="col-lg-offset-4 col-md-offset-4 col-sm-offset-2 col-xs-12 col-sm-5 col-md-4">
          <h2>Search</h2>
          <form action="//www.canada.ca/en/sr/srb/sra.html" method="get" name="cse-search-box" role="search">
            <div class="form-group wb-srch-qry">
              <label for="wb-srch-q" class="wb-inv">Search Canadian Space Agency</label>
              <input name="dmn" value="asc-csa.gc.ca" type="hidden">
              <input id="wb-srch-q" list="wb-srch-q-ac" class="wb-srch-q form-control" name="allq" type="search" value="" size="34" maxlength="170" placeholder="Search Canadian Space Agency">
              <datalist id="wb-srch-q-ac"></datalist>
            </div>
            <div class="form-group submit">
              <button type="submit" id="wb-srch-sub" class="btn btn-primary btn-small" name="wb-srch-sub">
                <span class="glyphicon-search glyphicon"></span>
                <span class="wb-inv">Search</span></button>
            </div>
          </form>
        </section>
      </div>
    </div>
    <nav class="gcweb-menu" typeof="SiteNavigationElement">
        <div class="container">
        <h2 class="wb-inv">Menu</h2>
        <button type="button" aria-haspopup="true" aria-expanded="false" aria-label="Press the SPACEBAR to expand or the escape key to collapse this menu. Use the Up and Down arrow keys to choose a submenu item. Press the Enter or Right arrow key to expand it, or the Left arrow or Escape key to collapse it. Use the Up and Down arrow keys to choose an item on that level and the Enter key to access it."><span class="wb-inv">Main </span>Menu <span class="expicon glyphicon glyphicon-chevron-down"></span></button>
        <ul role="menu" aria-orientation="vertical" data-ajax-replace="https://wet-boew.github.io/themes-dist/GCWeb/ajax/sitemenu-v5-en.html" class="wb-init wb-data-ajax-replace-inited" id="wb-auto-3">

        <!-- Web Experience Toolkit (WET) / Boîte à outils de l'expérience Web (BOEW)
        wet-boew.github.io/wet-boew/License-en.html / wet-boew.github.io/wet-boew/Licence-fr.html -->
        <!-- DataAjaxFragmentStart -->
        '''+ gc_menu_items_en +'''
        <!-- DataAjaxFragmentEnd -->
        </ul>
        </div>
    </nav>
    '''+ gc_breadcrumb_en +'''
</header>
'''


gc_footer_en = '''
        <div class="row" style="background-color: white;">
        <div class="pagedetails container">
        <div class="col-sm-6 col-md-5 col-lg-4">
        <a href="https://www.asc-csa.gc.ca/eng/forms/information-request.asp" class="btn btn-default">Report a problem on this page</a>
        </div>
        <dl id="wb-dtmd">
        <dt>Date modified:&#32;</dt>
        <dd><time property="dateModified">2023-03-14</time></dd>
        </dl>
        </div>
        </div>

        <div class="landscape">
        <nav class="container wb-navcurr" aria-label="Footer navigation">
				<h3 class="text-white">Government of Canada</h3>
				<ul class="list-col-xs-1 list-col-sm-2 list-col-md-3">
					<li><a href="https://www.canada.ca/en/contact.html">All contacts</a></li>
					<li><a href="https://www.canada.ca/en/government/dept.html">Departments and agencies</a></li>
					<li><a href="https://www.canada.ca/en/government/system.html">About government</a></li>
				</ul>
				<h4 class="text-white"><span class="wb-inv">Themes and topics</span></h4>
				<ul class="list-unstyled colcount-sm-2 colcount-md-3">
					<li><a href="https://www.canada.ca/en/services/jobs.html">Jobs</a></li>
					<li><a href="https://www.canada.ca/en/services/immigration-citizenship.html">Immigration and citizenship</a></li>
					<li><a href="https://travel.gc.ca/">Travel and tourism</a></li>
					<li><a href="https://www.canada.ca/en/services/business.html">Business</a></li>
					<li><a href="https://www.canada.ca/en/services/benefits.html">Benefits</a></li>
					<li><a href="https://www.canada.ca/en/services/health.html">Health</a></li>
					<li><a href="https://www.canada.ca/en/services/taxes.html">Taxes</a></li>
					<li><a href="https://www.canada.ca/en/services/environment.html">Environment and natural resources</a></li>
					<li><a href="https://www.canada.ca/en/services/defence.html">National security and defence</a></li>
					<li><a href="https://www.canada.ca/en/services/culture.html">Culture, history and sport</a></li>
					<li><a href="https://www.canada.ca/en/services/policing.html">Policing, justice and emergencies</a></li>
					<li><a href="https://www.canada.ca/en/services/transport.html">Transport and infrastructure</a></li>
					<li><a href="https://international.gc.ca/world-monde/index.aspx?lang=eng">Canada and the world</a></li>
					<li><a href="https://www.canada.ca/en/services/finance.html">Money and finance</a></li>
					<li><a href="https://www.canada.ca/en/services/science.html">Science and innovation</a></li>
					<li><a href="https://www.canada.ca/en/services/indigenous-peoples.html">Indigenous peoples</a></li>
					<li><a href="https://www.canada.ca/en/services/veterans.html">Veterans and military</a></li>
					<li><a href="https://www.canada.ca/en/services/youth.html">Youth</a></li>
				</ul>
			</nav>
        </div>
        <div class="brand">
            <div class="container">
                <div class="row">
                    <nav class="col-md-10 ftr-urlt-lnk">
                        <h2 class="wb-inv">About this site</h2>
                        <ul>
                            <li><a href="https://www.canada.ca/en/social.html" style="color: #223677">Social media</a></li>
                            <li><a href="https://www.canada.ca/en/mobile.html" style="color: #223677">Mobile applications</a></li>
                            <li><a href="https://www.canada.ca/en/government/about.html" style="color: #223677">About Canada.ca</a></li>
                            <li><a href="https://www.canada.ca/en/transparency/terms.html" style="color: #223677">Terms and conditions</a></li>
                            <li><a href="https://www.canada.ca/en/transparency/privacy.html" style="color: #223677">Privacy</a></li>
                        </ul>
                    </nav>
                    <div class="col-xs-6 visible-sm visible-xs tofpg">
                        <a href="#wb-cont">Top of page <span class="glyphicon glyphicon-chevron-up"></span></a>
                    </div>
                    <div class="col-xs-6 col-md-2 text-right">
                        <img src="https://canada.ca/etc/designs/canada/wet-boew/assets/wmms-blk.svg" alt="Symbol of the Government of Canada">
                    </div>
                </div>
            </div>
        </div>
'''

gc_menu_items_fr='''
<li role="presentation">
    <a role="menuitem" tabindex="0" aria-haspopup="true" aria-controls="gc-mnu-jobs" aria-expanded="true" href="#">Emplois et milieu de travail</a>
  <ul id="gc-mnu-jobs" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/emplois.html">Emplois<span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/emplois/opportunites.html">Trouver un emploi</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/emplois/formation.html">Formation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/gestion-entreprise">Embauche et gestion de personnel</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/demarrage-entreprise">Démarrage d'entreprise</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/emplois/milieu-travail.html">Normes en milieu de travail</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/pensions.html">Pensions et retraite</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/ae.html">Prestations d'assurance-emploi et congés</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-jobs-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-jobs-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/emploi-developpement-social/programmes/assurance-emploi/ae-liste/assurance-emploi-re/acceder-re.html">Voir vos Relevés d’emploi</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/emploi-developpement-social/services/numero-assurance-sociale.html">Demander un numéro d’assurance-sociale</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/emploi-developpement-social/services/travailleurs-etrangers.html">Embaucher un travailleur étranger temporaire</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/immigrer-canada/entree-express.html">Immigrer en tant que travailleur qualifié</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-cit" aria-expanded="false" href="#">Immigration et citoyenneté</a>
  <ul id="gc-mnu-cit" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/immigration-citoyennete.html">Immigration<span class="hidden-xs hidden-sm"> et citoyenneté</span><span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/demande.html">Ma demande</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/visiter-canada.html">Visiter</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/immigrer-canada.html">Immigrer</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/travailler-canada.html">Travailler</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/etudier-canada.html">Étudier</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/citoyennete-canadienne.html">Citoyenneté</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/nouveaux-immigrants.html">Nouveaux immigrants</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/canadiens.html">Canadiens</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/refugies.html">Réfugiés et octroi de l’asile</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/immigration-citoyennete/application-loi-infractions.html">Application de la loi et infractions</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-cit-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-cit-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/demande/compte.html">Se connecter ou créer un compte pour présenter une demande en ligne</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/demande/verifier-etat.html">Vérifier l’état de sa demande</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cic.gc.ca/francais/information/delais/index.asp">Vérifier les délais de traitement des demandes</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/demande/formulaires-demande-guides.html">Trouver un formulaire de demande</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cic.gc.ca/francais/information/frais/index.asp">Payer les frais</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cic.gc.ca/francais/visiter/visas.asp">Déterminer si vous avez besoin d’une AVE ou d’un visa pour visiter le Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cic.gc.ca/francais/centre-aide/index-en-vedette-can.asp">Trouver réponse à ses questions dans le Centre d’aide</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-travel" aria-expanded="false" href="#">Voyage et tourisme</a>
  <ul id="gc-mnu-travel" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/">Voyage<span class="hidden-xs hidden-sm"> et tourisme</span><span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/voyager/avertissements">Conseils aux voyageurs et avertissements</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/tourisme-canadien">Attraits touristiques, événements et expériences au Canada</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/immigration-refugies-citoyennete/services/passeports-canadiens.html">Passeports canadiens</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/voyager">Voyager à l’étranger</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/avion">Voyager en avion</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/retour">Retour au Canada</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/assistance">Assistance à l’étranger</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/restez-branches">Restez branchés</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/visiter">Visiter le Canada</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-travel-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-travel-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/voyager/enfant/lettre-de-consentement">Lettre de consentement pour les enfants qui voyagent à l’étranger</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.cbsa-asfc.gc.ca/bwt-taf/menu-fra.html">Temps d’attente à la frontière Canada - États-Unis</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/voyager/inscription">Inscrivez-vous comme Canadien à l’étranger</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.cbsa-asfc.gc.ca/prog/nexus/application-demande-fra.html">Adhérez à NEXUS</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/retour/douane/ce-que-vous-pouvez-ramener-au-canada">Ce que vous pouvez ramener au Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/assistance/ambassades-consulats">Communiquer avec une ambassade ou un consulat</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/voyager/le-cannabis-et-les-voyages-a-l-etranger">Le cannabis et les voyages à l’étranger</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-biz" aria-expanded="false" href="#">Entreprises et industrie</a>
  <ul id="gc-mnu-biz" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises.html">Entreprises<span class="hidden-xs hidden-sm"> et industrie</span><span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/lancer.html">Démarrage d'entreprise</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/subventions.html">Subventions et financement pour les entreprises</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/impots.html">Taxes et impôt des entreprises</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/societes-de-regime-federal.html">Sociétés de régime fédéral</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/engager.html">Embauche et gestion de personnel</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/commerce.html">Commerce international et investissements</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/permis.html">Permis, licences et règlements</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/faire-affaire.html">Faire affaire avec le gouvernement</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science/innovation.html">Recherche-développement et innovation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/recherche.html">Recherche et renseignements d'affaires</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/pi.html">Propriété intellectuelle et droit d'auteur</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/maintenirfairecroitreameliorerentreprise.html">Administration de votre entreprise</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/proteger.html">Protection de votre entreprise</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/faillites.html">Insolvabilité pour les entreprises</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-biz-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-biz-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/fdrlCrpSrch.html">Trouver une société</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.cbsa-asfc.gc.ca/prog/manif/portal-portail-fra.html">Déclarer vos produits importés</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.ic.gc.ca/app/opic-cipo/trdmrks/srch/accueil?lang=fra">Chercher des marques de commerce</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/2018/html/tblmod-1-fra.html">Réviser les tarifs des douanes pour l’importation de produits</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.ic.gc.ca/opic-cipo/cpd/eng/introduction.html">Trouver un brevet</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.cbsa-asfc.gc.ca/comm-fra.html">Importer et exporter à partir du Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.ic.gc.ca/eic/site/075.nsf/fra/accueil">Trouver un nom pour votre compagnie</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.ic.gc.ca/app/scr/cc/CorporationsCanada/hm.html?f=&amp;selectedDirectorUuid=%3BselectedIncorporatorUuid%3D&amp;metricsId=GTM-WQQH22">Apporter des changements à votre société (Centre de dépôt en ligne)</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-benny" aria-expanded="false" href="#">Prestations</a>
  <ul id="gc-mnu-benny" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations.html">Prestations<span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/ae.html">Prestations d'assurance-emploi et congés</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/famille.html">Prestations pour familles et proches aidants</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/pensionspubliques.html">Pensions publiques</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/etudes.html">Éducation et aide aux étudiants</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/logement.html">Prestations relatives au logement</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/handicap.html">Prestations relatives aux personnes handicapées</a></li>

    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.prestationsducanada.gc.ca/">Chercheur de prestations</a></li>
<li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/calendrier.html">Dates de paiement des prestations</a></li>

    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-benny-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-benny-sub" role="menu" aria-orientation="vertical">

        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/ae/assurance-emploi-reguliere.html">Présenter une demande d’assurance-emploi</a></li>

        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/education/aide-etudiants/bourses-prets.html">Faire une demande de bourses et de prêts  d’études</a></li>
       <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/gouvernement/ouvrir-session-dossier-compte-en-ligne.html">Ouvrir une session pour un compte en ligne  du gouvernement du Canada</a></li>

        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.tpsgc-pwgsc.gc.ca/recgen/txt/depot-deposit-fra.html">Inscrivez-vous au dépôt direct</a></li>

        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/prestations-enfants-familles/calculateur-prestations-enfants-familles.html">Calculateur de prestations pour enfants et familles</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/prestations/ae/assurance-emploi-declaration-internet.html">Soumettre une déclaration d’assurance-emploi</a></li>

      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-health" aria-expanded="false" href="#">Santé</a>
  <ul id="gc-mnu-health" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante.html">Santé<span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante/aliments-et-nutrition.html">Aliments et nutrition</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/sante-publique/services/maladies.html">Maladies et affections</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/sante-publique/sujets/immunisation-et-vaccins.html">Vaccins et immunisation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante/medicaments-et-produits-sante.html">Médicaments et produits de santé</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante/securite-produits.html">Sécurité des produits</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante/securite-et-risque-pour-sante.html">Sécurité et risque pour la santé</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante/vie-saine.html">Vie saine</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante/sante-autochtones.html">Santé des Autochtones</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante/systeme-et-services-sante.html">Système et services de santé</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/sante/science-recherche-et-donnees.html">Science, recherche et données</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-health-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-health-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/sante-canada/services/drogues-medicaments/cannabis/titulaires-licences-demandeurs-industrie/cultivateurs-transformateurs-vendeurs-autorises.html">Cultivateurs, transformateurs et vendeurs de cannabis qui détiennent une licence</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.canadiensensante.gc.ca/recall-alert-rappel-avis/index-fra.php">Rappels d'aliments et de produits et alertes de sécurité</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/sante-canada/services/guides-alimentaires-canada.html">Guide alimentaire du Canada</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-taxes" aria-expanded="false" href="#">Impôts</a>
  <ul id="gc-mnu-taxes" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/impots.html">Impôts<span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/impots/impot-sur-le-revenu.html">Impôt sur le revenu</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/impot/entreprises/sujets/tps-tvh-entreprises.html">TPS/TVH</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/impot/entreprises/sujets/retenues-paie.html">Retenues sur la paie</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/impots/numero-dentreprise.html">Numéro d'entreprise</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/impots/regimes-depargne-et-de-pension.html">Régimes d’épargne et de pension</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/impots/prestations-pour-enfants-et-familles.html">Prestations pour enfants et familles</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/impots/taxes-daccise-droits-et-prelevements.html">Taxes d’accise, droits et prélèvements</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/impots/bienfaisance.html">Organismes de bienfaisance et dons</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-taxes-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-taxes-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/services-electroniques/services-electroniques-particuliers/dossier-particuliers.html">Mon dossier</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/services-electroniques/services-electroniques-entreprises/dossier-entreprise.html">Mon dossier d'entreprise</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/services-electroniques/representer-client.html">Représenter un client</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/services-electroniques/services-electroniques-entreprises/impotnet-tps-tvh.html">Transmettre une déclaration de TPS/TVH (IMPÔTNET)</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/faire-paiement-a-agence-revenu-canada.html">Faire un paiement à l'Agence du revenu du Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/prestations-enfants-familles/dates-versement-prestations.html">Trouver la date du prochain versement des prestations</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-enviro" aria-expanded="false" href="#">Environnement et ressources naturelles</a>
  <ul id="gc-mnu-enviro" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement.html">Environnement<span class="hidden-xs hidden-sm"> et ressources naturelles</span><span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement/meteo.html">Météo, climat et catastrophes naturelles</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement/energie.html">Énergie</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement/ressources-naturelles.html">Ressources naturelles</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement/pratiques-agricoles.html">Pratiques agricoles</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement/peches.html">Pêches</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement/faune-flore-especes.html">Faune, flore et espèces</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement/pollution-gestion-dechets.html">Pollution et gestion des déchets</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/environnement/conservation.html">Conservation et protection de l'environnement</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-enviro-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-enviro-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://meteo.gc.ca/canada_f.html">Prévisions météo locales</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.rncan.gc.ca/energie/efficacite/transports/20997">Véhicules écoénergétiques</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.rncan.gc.ca/maisons">Efficacité énergétique des maisons</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.registrelep-sararegistry.gc.ca/species/default_f.cfm">Espèces en péril</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/environnement-changement-climatique/services/meteo-saisonniere-dangereuse.html">Préparation aux conditions météorologiques dangereuses</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-defence" aria-expanded="false" href="#">Sécurité nationale et défense</a>
  <ul id="gc-mnu-defence" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/defense.html"><span class="hidden-xs hidden-sm">Sécurité nationale et défense</span><span class="visible-xs-inline visible-sm-inline">Défense : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/defense/securitenationale.html">Sécurité nationale</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/defense/fac.html">Forces armées canadiennes</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/defense/achat-mise-a-niveau-equipement-defense.html">Achat et mise à niveau d’équipement de la Défense</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/surete-transports.html">Sûreté des transports</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/defense/securiserfrontiere.html">Sécuriser la frontière</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/defense/cybersecurite.html">Cybersécurité</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/defense/emplois.html">Emplois en sécurité nationale et en défense</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/gouvernement/fonctionpublique/avantagesmilitaires.html">Services et avantages sociaux du personnel militaire</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-defence-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-defence-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://forces.ca/fr/carrieres/">Emplois dans les Forces armées canadiennes</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/ministere-defense-nationale/services/histoire-militaire/histoire-patrimoine/insignes-drapeaux/grades/insignes-grade-fonction.html">Grades militaires</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/defense/fac/equipement.html">Équipement de la Défense</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.cadets.ca/fr/joignez-vous/cadets.page">Devenir cadet</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://dgpaapp.forces.gc.ca/fr/politique-defense-canada/index.asp">Politique de défense du Canada</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-culture" aria-expanded="false" href="#">Culture, histoire et sport</a>
  <ul id="gc-mnu-culture" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture.html">Culture<span class="hidden-xs hidden-sm">, histoire et sport</span><span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/patrimoine-canadien/services/financement.html">Financement - Culture, histoire et sport</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/evenements-celebrations-commemorations.html">Événements, célébrations et commémorations</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/attraits-culturels.html">Lieux et attraits culturels</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/identite-canadienne-societe.html">Identité canadienne et société</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/sport.html">Sport</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/histoire-patrimoine.html">Histoire et patrimoine</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/arts-media.html">Arts et média</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/programmes-culturels-jeunes.html">Programmes culturels pour les jeunes</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/commerce-investissement-culturels.html">Commerce et investissement culturels</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-culture-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-culture-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.veterans.gc.ca/fra/remembrance/memorials/canadian-virtual-war-memorial">Visitez le Mémorial virtuel de guerre du Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/identite-canadienne-societe/hymnes-symboles.html">Hymnes et symboles du Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://crtc.gc.ca/fra/8045/d2018.htm">Trouvez une décision du CRTC</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.bac-lac.gc.ca/fra/recherche/Pages/recherche-ancetres.aspx">Faites des recherches sur votre histoire familiale</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.bac-lac.gc.ca/fra/recensements/Pages/recensements.aspx">Cherchez des documents de recensement</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/culture/attraits-culturels/attraits-capitale-canada.html">Lieux et attraits dans la capitale du Canada</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-policing" aria-expanded="false" href="#">Services de police, justice et urgences</a>
  <ul id="gc-mnu-policing" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police.html">Services de police<span class="hidden-xs hidden-sm">, justice et urgences</span><span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police/servicespolice.html">Services de police</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police/justice.html">Justice</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police/urgences.html">Urgences</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police/correctionnels.html">Services correctionnels</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police/liberationconditionnelle.html">Libération conditionnelle, suspension du casier, radiation et clémence</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police/victimes.html">Victimes d'actes criminels</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-policing-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-policing-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.rcmp-grc.gc.ca/cfp-pcaf/online_en-ligne/index-fra.htm">Demander ou renouveler un permis d'arme à feu</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.rcmp-grc.gc.ca/fr/verification-casier-judiciaire">Obtenir une attestation de vérification de casier judiciaire</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/commission-liberations-conditionnelles/services/suspension-du-casier/guide-et-formulaires-de-demande.html">Demander la suspension d’un casier judiciaire</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.preparez-vous.gc.ca/cnt/hzd/drng-fr.aspx">Que faire durant une urgence</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police/servicespolice/securite-communautaire-police/conduite-facultes-affaiblies.html">Connaissez la loi sur la conduite avec facultés affaiblies</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/police/servicespolice/aider-resoudre-un-crime.html">Aidez à résoudre un crime</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-trans" aria-expanded="false" href="#">Transport et infrastructure</a>
  <ul id="gc-mnu-trans" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/transport.html">Transport<span class="hidden-xs hidden-sm"> et infrastructure</span><span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/aviation.html">Aviation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/maritime.html">Transport maritime</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/routier.html">Transport routier</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/ferroviaire.html">Transport ferroviaire</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/marchandises-dangereuses.html">Marchandises dangereuses</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/infrastructures.html">Infrastructure</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-trans-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-trans-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/aviation/securite-drones.html">Sécurité des drones</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/surete-transports/aerienne/articles-interdits-bord-avion.html">Articles interdits à bord d’un avion</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fra/securitemaritime/epe-immabatiments-menu-728.htm">Immatriculer votre bâtiment</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/services/routier/securite-sieges-auto-enfants.html">Sécurité des sièges d'auto pour enfants</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fra/tmd/clair-tdesm-211.htm">Transporter des marchandises dangereuses - Règlements</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.tc.gc.ca/fr/transports-canada/organisation/lois-reglements/reglements/sor-96-433.html">Règlement de l’aviation canadien</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-canworld" aria-expanded="false" href="#">Canada et le monde</a>
  <ul id="gc-mnu-canworld" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/index.aspx?lang=fra">Le Canada et le monde<span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/offices-bureaux/index.aspx?lang=fra">Bureaux internationaux et contacts d’urgence</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://international.gc.ca/world-monde/study_work_travel-etude_travail_voyage/index.aspx?lang=fra">Étude, travail et voyage partout dans le monde</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/funding-financement/index.aspx?lang=frag">Financement d’initiatives internationales</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/issues_development-enjeux_developpement/index.aspx?lang=fra">Enjeux mondiaux et aide internationale</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://www.canada.ca/fr/services/entreprises/commerce/index.html">Commerce international et investissement</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/international_relations-relations_internationales/index.aspx?lang=fra">Relations internationales</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/country-pays/index.aspx?lang=fra">Information par pays et territoires</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://international.gc.ca/world-monde/stories-histoires/index.aspx?lang=fra">Histoires</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-canworld-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-canworld-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://scholarships-bourses.gc.ca/scholarships-bourses/non_can/opportunities-opportunites.aspx?lang=fra">Trouver une bourse d’études canadienne en tant qu’étudiant international</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://educanada.ca/index.aspx?lang=fra">Trouver des occasions d’étude ou de recherche au Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://voyage.gc.ca/assistance/ambassades-consulats">Communiquer avec une ambassade ou un consulat</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/world-monde/study_work_travel-etude_travail_voyage/authentication-authentification/index.aspx?lang=fra">Authentifier un document</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://international.gc.ca/protocol-protocole/reps.aspx?lang=fra">Communiquer avec un représentant étranger au Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://treaty-accord.gc.ca/index.aspx?Lang=fra">Traités internationaux signés par le Canada</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-money" aria-expanded="false" href="#">Argent et finances</a>
  <ul id="gc-mnu-money" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance.html"><span class="hidden-xs hidden-sm">Argent et finances</span><span class="visible-xs-inline visible-sm-inline">Finances : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/gerer.html">Gérer votre argent</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/dettes.html">Dettes et emprunts</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/epargne.html">Épargne et investissement</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/financementetudes.html">Financement des études</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/pensions.html">Pensions et retraite</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/fraude.html">Protection contre la fraude et les escroqueries</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/outils.html">Calculatrices et outils financiers</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-consommation-matiere-financiere/services/programmes-litteratie-financiere.html">Programmes de littératie financière</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/questions-consommation.html">Questions de consommation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/finance/faillite.html">Insolvabilité</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/impots.html">Impôts</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/gouvernement/systeme/finances.html">Finances publiques</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/subventions.html">Subventions et financement pour les entreprises</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/permis/secteursindustriereglementationfederale/regleservicesfinanciers.html">Réglementation des services financiers et monétaires</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-money-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-money-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.ic.gc.ca/app/scr/bsf-osb/ins/connexion.html?lang=fra">Trouver un dossier de faillite ou d’insolvabilité</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/emplois/education/aide-financiere-etudiants/pret-etudiants.html">Prêts étudiants</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.tpsgc-pwgsc.gc.ca/recgen/txt/depot-deposit-fra.html">Inscrivez-vous au dépôt direct</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-consommation-matiere-financiere/services/hypotheques.html">Obtenir des renseignements sur les hypothèques</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-consommation-matiere-financiere/services/dossier-pointage-credit.html">Dossiers et cotes de crédit</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://itools-ioutils.fcac-acfc.gc.ca/BC-CB/NetInc-RevNet-fra.aspx">Faire un budget</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/agence-revenu/services/impot/administrateurs-regimes-enregistres/fesp/plafonds-cd-reer-rpdb-celi-mgap.html">Taux et limites de contribution</a></li>
      </ul>
    </li>
  </ul>
</li>
<li role="presentation"> <a role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-science" aria-expanded="false" href="#">Science et innovation</a>
  <ul id="gc-mnu-science" role="menu" aria-orientation="vertical">
    <li role="presentation"> <a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science.html">Science<span class="hidden-xs hidden-sm"> et innovation</span><span class="visible-xs-inline visible-sm-inline"> : accueil</span></a> </li>
    <li role="separator"></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science/financementrecherche.html">Financement, subventions et prix pour la recherche</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science/themesscientifiques.html">Thèmes scientifiques</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science/donnees-ouvertes.html">Données ouvertes, statistiques et archives</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science/instituts.html">Instituts et établissements de recherches</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science/innovation.html">R-D et innovation</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/entreprises/pi.html">Propriété intellectuelle et droit d'auteur</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science/repertoirescientifiques.html">Répertoire des scientifiques et des professionnels de la recherche</a></li>
    <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.canada.ca/fr/services/science/ressourcespedagogiques.html">Ressources pédagogiques scientifiques</a></li>
    <li role="separator" aria-orientation="vertical"></li>
    <li role="presentation"> <a data-keep-expanded="md-min" href="#" role="menuitem" tabindex="-1" aria-haspopup="true" aria-controls="gc-mnu-science-sub" aria-expanded="true">En demande</a>
      <ul id="gc-mnu-science-sub" role="menu" aria-orientation="vertical">
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrc-cnrc.gc.ca/fra/publications/centre_codes/2015_code_national_batiment.html">Code national du bâtiment</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrc-cnrc.gc.ca/fra/services/heure/horloge_web.html#tzpanel-4">Heures officielles au Canada</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrc-cnrc.gc.ca/fra/services/levers/index.html">Trouver les heures de levers et de couchers du soleil</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://www.nrc-cnrc.gc.ca/fra/pari/services/aide_financiere.html">Bourses pour l’innovation technologique (PARI)</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="https://science-libraries.canada.ca/fra/accueil/">Bibliothèque scientifique fédérale</a></li>
        <li role="presentation"><a role="menuitem" tabindex="-1" href="http://asc-csa.gc.ca/fra/astronomie/auroramax/hd-480.asp">Aurores boréales en direct</a></li>
      </ul>
    </li>
  </ul>
</li>
'''

gc_header_fr = '''
<div class='global-header'>
<nav aria-label='menu accessible'>
  <ul id="wb-tphp" class="wb-init wb-disable-inited">
	  <li class="wb-slc"><a class="wb-sl" href="#react-entry-point">Passer au contenu principal</a></li>
	  <!--<li class="wb-slc"><a class="wb-sl" href="#wb-info">Passer à « Au sujet du gouvernement »</a></li>
    <li class="wb-slc"><a class="wb-sl" href="?wbdisable=true" rel="alternate">Passer à la version HTML simplifiée</a></li>-->
  </ul>
</nav>
<header aria-label='En-tête de page' >
	<div id="wb-bnr" class="container">
		<div class="row">

			<section id="wb-lng" class="col-xs-3 col-sm-12 pull-right text-right">
    <h2 class="wb-inv">Sélection de la langue</h2>
    <div class="row">
        <div class="col-md-12">
            <ul class="list-inline mrgn-bttm-0">
                <li>
                    <a lang="en" href="'''+ app_config.EN_LINK +'''">
                            <span class="hidden-xs">English</span>
                            <abbr title="English" class="visible-xs h3 mrgn-tp-sm mrgn-bttm-0 text-uppercase">en</abbr>
                    </a>
                </li>


            </ul>
        </div>
    </div>
</section>
				<div class="brand col-xs-9 col-sm-5 col-md-4" property="publisher" resource="#wb-publisher" typeof="GovernmentOrganization">



						<link href="https://www.canada.ca/content/canadasite/fr.html" property="url">

							<img src="https://www.canada.ca/etc/designs/canada/wet-boew/assets/sig-blk-fr.svg" alt="Gouvernement du Canada" property="logo">
							<span class="wb-inv"> /

								<span lang="en">Government of Canada</span>
							</span>


					<meta property="name" content="Gouvernement du Canada">
					<meta property="areaServed" typeof="Country" content="Canada">
					<link property="logo" href="https://www.canada.ca/etc/designs/canada/wet-boew/assets/wmms-blk.svg">
				</div>
				<section id="wb-srch" class="col-lg-offset-4 col-md-offset-4 col-sm-offset-2 col-xs-12 col-sm-5 col-md-4">
					<h2>Recherche</h2>

<form action="https://www.canada.ca/fr/sr/srb.html" method="get" name="cse-search-box" role="search">
	<div class="form-group wb-srch-qry">
		<label for="wb-srch-q" class="wb-inv">Rechercher dans Canada.ca</label>
		<input name="cdn" value="canada" type="hidden">
		<input name="st" value="s" type="hidden">
		<input name="num" value="10" type="hidden">
		<input name="langs" value="fr" type="hidden">
		<input name="st1rt" value="1" type="hidden">
		<input name="s5bm3ts21rch" value="x" type="hidden">

			<input id="wb-srch-q" list="wb-srch-q-ac" class="wb-srch-q form-control" name="q" type="search" value="" size="34" maxlength="170" placeholder="Rechercher dans Canada.ca">


		<input type="hidden" name="_charset_" value="UTF-8">

		<datalist id="wb-srch-q-ac">
		</datalist>
	</div>
	<div class="form-group submit">
	<button type="submit" id="wb-srch-sub" class="btn btn-primary btn-small" name="wb-srch-sub"><span class="glyphicon-search glyphicon"></span><span class="wb-inv">Recherche</span></button>
	</div>
</form>

				</section>
		</div>
	</div>


	<nav class="gcweb-v2 gcweb-menu wb-init gcweb-menu-inited" aria-label="navigation principale" typeof="SiteNavigationElement" id="wb-auto-2"><div class="container">
		<h2 class="wb-inv">Menu</h2>
		<button type="button" aria-haspopup="true" aria-expanded="false" aria-label="Appuyez sur la barre d'espacement pour ouvrir ou sur la touche d'échappement pour fermer le menu. Utilisez les flèches haut et bas pour choisir un élément de sous-menu. Appuyez sur la touche Entrée ou sur la flèche vers la droite pour le développer, ou sur la flèche vers la gauche ou la touche Échap pour le réduire. Utilisez les flèches haut et bas pour choisir un élément de ce niveau et la touche Entrée pour y accéder.">Menu<span class="wb-inv"> principal</span> <span class="expicon glyphicon glyphicon-chevron-down"></span></button>
		<ul role="menu" aria-orientation="vertical" data-ajax-replace="https://www.canada.ca/content/dam/canada/sitemenu/sitemenu-v2-fr.html" class="wb-init wb-data-ajax-replace-inited" id="wb-auto-3">
    '''+ gc_menu_items_fr +'''
    </ul>

	</div></nav>
	'''+ gc_breadcrumb_fr +'''
	<div data-ajax-replace="https://www.canada.ca/bin/canada/alert/messages.fr.html" class="original wb-init wb-data-ajax-replace-inited" id="wb-auto-4"></div>




</header>
</div>
'''

gc_header_fr_old = '''
<header>
				<div id="wb-bnr" class="container">
					<div class="row">
						<section id="wb-lng" class="col-xs-3 col-sm-12 pull-right text-right">
							<h2 class="wb-inv">Sélection de la langue</h2>
							<ul class="list-inline mrgn-bttm-0">
								<li>
									<a lang="en" hreflang="en" href="'''+ app_config.EN_LINK +'''">
									<span class="hidden-xs">English</span>
									<abbr title="English" class="visible-xs h3 mrgn-tp-sm mrgn-bttm-0 text-uppercase">en</abbr>
									</a>
								</li>
							</ul>
						</section>
						<div class="brand col-xs-9 col-sm-5 col-md-4" property="publisher" typeof="GovernmentOrganization">
							<a href="https://www.canada.ca/en.html" property="URL">
								<img src="assets/gc_theme_cdn/assets/sig-blk-fr.svg" alt="Gouvernement du Canada" property="logo">
									<span class="wb-inv"> /
										<span lang="en">Government of Canada</span>
									</span></a>
							<meta property="name" content="Gouvernement du Canada">
							<meta property="areaServed" typeof="Country" content="Canada">
							<link property="logo" href="assets/gc_theme_cdn/assets/sig-blk-fr.svg">
						</div>
						<section id="wb-srch" class="col-lg-offset-4 col-md-offset-4 col-sm-offset-2 col-xs-12 col-sm-5 col-md-4">
							<h2>Recherche</h2>
							<form action="//www.canada.ca/fr/sr/srb/sra.html" method="get" name="cse-search-box" role="search">
								<div class="form-group wb-srch-qry">
									<label for="wb-srch-q" class="wb-inv">Rechercher dans l'Agence spatiale canadienne</label>
									<input name="dmn" value="asc-csa.gc.ca" type="hidden">
									<input id="wb-srch-q" list="wb-srch-q-ac" class="wb-srch-q form-control" name="allq" type="search" value="" size="34" maxlength="170" placeholder="Rechercher dans l'Agence spatiale canadienne">
									<datalist id="wb-srch-q-ac"></datalist>
								</div>
								<div class="form-group submit">
									<button type="submit" id="wb-srch-sub" class="btn btn-primary btn-small" name="wb-srch-sub">
										<span class="glyphicon-search glyphicon"></span>
										<span class="wb-inv">Recherche</span></button>
								</div>
							</form>
						</section>
					</div>
				</div>


	<nav class="gcweb-v2 gcweb-menu wb-init gcweb-menu-inited" typeof="SiteNavigationElement" id="wb-auto-2"><div class="container">
		<h2 class="wb-inv">Menu</h2>
		<button type="button" aria-haspopup="true" aria-expanded="false" aria-label="Appuyez sur la barre d'espacement pour ouvrir ou sur la touche d'échappement pour fermer le menu. Utilisez les flèches haut et bas pour choisir un élément de sous-menu. Appuyez sur la touche Entrée ou sur la flèche vers la droite pour le développer, ou sur la flèche vers la gauche ou la touche Échap pour le réduire. Utilisez les flèches haut et bas pour choisir un élément de ce niveau et la touche Entrée pour y accéder.">Menu<span class="wb-inv"> principal</span> <span class="expicon glyphicon glyphicon-chevron-down"></span></button>
		<ul role="menu" aria-orientation="vertical" data-ajax-replace="/content/dam/canada/sitemenu/sitemenu-v2-fr.html" class="wb-init wb-data-ajax-replace-inited" id="wb-auto-3">
    '''+ gc_menu_items_fr +'''
    </ul>
	</div></nav>



	'''+ gc_breadcrumb_fr +'''
	<div data-ajax-replace="/bin/canada/alert/messages.fr.html" class="original wb-init wb-data-ajax-replace-inited" id="wb-auto-4"></div>

</header>
'''

gc_footer_fr = '''
        <div class="row" style="background-color: white;">
        <div class="pagedetails container">
        <div class="col-sm-6 col-md-5 col-lg-4">
        <a href="https://www.asc-csa.gc.ca/fra/formulaires/demande-information.asp" class="btn btn-default">Signaler un problème sur cette page</a>
        </div>
        <dl id="wb-dtmd">
        <dt>Date de modification:&#32;</dt>
        <dd><time property="dateModified">2023-03-14</time></dd>
        </dl>
        </div>
        </div>

        <div class="landscape">
        <nav class="container wb-navcurr" aria-label="Navigation en bas de page">
				<h3 class="text-white">Gouvernement du Canada</h3>
				<ul class="list-col-xs-1 list-col-sm-2 list-col-md-3">
                    <li><a href="https://www.canada.ca/fr/contact.html">Toutes les coordonnées</a></li>
					<li><a href="https://www.canada.ca/fr/gouvernement/min.html">Ministères et organismes</a></li>
					<li><a href="https://www.canada.ca/fr/gouvernement/systeme.html">À propos du gouvernement</a></li></ul>
				<h4 class="text-white"><span class="wb-inv">Thèmes et sujets</span></h4>
				<ul class="list-unstyled colcount-sm-2 colcount-md-3">
                    <li><a href="https://www.canada.ca/fr/services/emplois.html">Emplois</a></li>
					<li><a href="https://www.canada.ca/fr/services/immigration-citoyennete.html">Immigration et citoyenneté</a></li>
					<li><a href="https://voyage.gc.ca/">Voyage et tourisme</a></li>
					<li><a href="https://www.canada.ca/fr/services/entreprises.html">Entreprises</a></li>
					<li><a href="https://www.canada.ca/fr/services/prestations.html">Prestations</a></li>
					<li><a href="https://www.canada.ca/fr/services/sante.html">Santé</a></li>
					<li><a href="https://www.canada.ca/fr/services/impots.html">Impôts</a></li>
					<li><a href="https://www.canada.ca/fr/services/environnement.html">Environnement et ressources naturelles</a></li>
					<li><a href="https://www.canada.ca/fr/services/defense.html">Sécurité nationale et défense</a></li>
					<li><a href="https://www.canada.ca/fr/services/culture.html">Culture, histoire et sport</a></li>
					<li><a href="https://www.canada.ca/fr/services/police.html">Services de police, justice et urgences</a></li>
					<li><a href="https://www.canada.ca/fr/services/transport.html">Transport et infrastructure</a></li>
					<li><a href="https://www.international.gc.ca/world-monde/index.aspx?lang=fra">Le Canada et le monde</a></li>
					<li><a href="https://www.canada.ca/fr/services/finance.html">Argent et finance</a></li>
					<li><a href="https://www.canada.ca/fr/services/science.html">Science et innovation</a></li>
					<li><a href="https://www.canada.ca/fr/services/autochtones.html">Autochtones</a></li>
					<li><a href="https://www.canada.ca/fr/services/veterans.html">Vétérans et militaires</a></li>
					<li><a href="https://www.canada.ca/fr/services/jeunesse.html">Jeunesse</a></li></ul>
			</nav>
        </div>
        <div class="brand">
            <div class="container">
                <div class="row">
                    <nav class="col-md-10 ftr-urlt-lnk">
                        <h2 class="wb-inv">À propos de ce site</h2>
                        <ul>
                            <li><a href="https://www.canada.ca/fr/sociaux.html" style="color: #223677">Médias sociaux</a></li>
                            <li><a href="https://www.canada.ca/fr/mobile.html" style="color: #223677">Applications mobiles</a></li>
                            <li><a href="https://www.canada.ca/fr/gouvernement/a-propos.html" style="color: #223677">À propos de Canada.ca</a></li>
                            <li><a href="https://www.canada.ca/fr/transparence/avis.html" style="color: #223677">Avis</a></li>
                            <li><a href="https://www.canada.ca/fr/transparence/confidentialite.html" style="color: #223677">Confidentialité</a></li>
                        </ul>
                    </nav>
                    <div class="col-xs-6 visible-sm visible-xs tofpg">
                        <a href="#wb-cont">Haut de la page <span class="glyphicon glyphicon-chevron-up"></span></a>
                    </div>
                    <div class="col-xs-6 col-md-2 text-right">
                        <img src="https://canada.ca/etc/designs/canada/wet-boew/assets/wmms-blk.svg" alt="Symbole du gouvernement du Canada">
                    </div>
                </div>
            </div>
        </div>
'''
