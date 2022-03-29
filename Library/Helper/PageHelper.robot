*** Settings ***
Documentation           Page helper file
Resource                ../Helper/CommonHelper.robot
Library                 ../Page/BillingAccount.py
Library                 ../Page/UsageAccount.py
Library                 ../Page/User.py
Library                 ../Page/Team.py
Library                 ../Page/Alert.py
Library                 ../Page/Integration.py
Library                 ../Page/SSO.py
Library                 ../Page/API.py
Library                 ../Page/Costs.py
Library                 ../Page/Resource.py
Library                 ../Page/Savings.py
Library                 ../Page/Compliance.py
Library                 ../Page/Security.py
Library                 ../Page/Utilization.py
Library                 ../Page/Coverage.py


*** Keywords ***

# -----Billing Account Related Helper ----- #
Billing Account.Perform action on Billing Account
   ${page}  get page handle
   [Arguments]      ${search_billing_ac}
   click billing menu     ${page}
   click billing admin    ${page}
   click billing button   ${page}
   click billing help     ${page}
   click create billing ac  ${page}
   click cloudformation     ${page}
   click gcp billing               ${page}
   click cancel billing             ${page}
   click search billing ac          ${page}
   fill search billing ac           ${page}     ${search_billing_ac}
   click billing ac download        ${page}
   click billing ui setting         ${page}


# -----Usage Account Related Helper ----- #
Usage Account.Perform action on Usage Account
   ${page}  get page handle
   click usage menu     ${page}
   click usage admin    ${page}
   click usage button   ${page}
   click usage help     ${page}
   click create usage ac  ${page}
   click_u_manual     ${page}
   click gcp usage      ${page}
   click cancel usage       ${page}
   click search usage ac    ${page}
   fill search usage ac     ${page}
   click usage ac download      ${page}
   click usage ui setting       ${page}


# -----User Related Helper ----- #
Users.Get Data from user
   ${page}      get page handle
   [Arguments]      ${u_name}       ${email_id}         ${user}
   click user menu  ${page}
   click admin          ${page}
   click user module    ${page}
   click user help      ${page}
   click create user    ${page}
   click name           ${page}
   fill name            ${page}         ${u_name}
   click email id       ${page}
   fill email id        ${page}         ${email_id}
   click select roles   ${page}
   click owner          ${page}
   click administrator  ${page}
   click name           ${page}
   click select team    ${page}
   click team owner     ${page}
   click name           ${page}
   click submit         ${page}
   click edit user      ${page}
   click cancel edit user   ${page}
   click delete user         ${page}
   click cancel delete user   ${page}
   click user search          ${page}
   fill user search           ${page}   ${user}
   click user download       ${page}
   click user ui setting     ${page}


# ----- Teams Related Helper ----- #
Teams.Get Data from team
     ${page}      get page handle
   [Arguments]      ${t_name}   ${description}   ${team}
   click team menu  ${page}
   click team admin     ${page}
   click team module    ${page}
   click team help      ${page}
   click create team    ${page}
   enter team name      ${page}     ${t_name}
   enter description    ${page}     ${description}
   click users                  ${page}
   select users                 ${page}
   click accounts               ${page}
   click t submit               ${page}
   click edit team              ${page}
   click cancel edit team       ${page}
   click delete team            ${page}
   click cancel delete team     ${page}
   click team search            ${page}
   fill team search             ${page}   ${team}
   click team download          ${page}
   click team ui setting        ${page}



# -----Alert Related Helper ----- #
Alerts.Perform action on Alert
   ${page}  get page handle
   [Arguments]      ${cost}       ${search}
   click alert menu     ${page}
   click alert admin    ${page}
   click on alerts      ${page}
   click alert help     ${page}
   click create alert   ${page}
   click alert rule     ${page}
   click daily cost     ${page}
   click provider       ${page}
   click of provider    ${page}
   click select drop    ${page}
   click gcp            ${page}
   click close dropdown  ${page}
   click is more than   ${page}
   click is going up by  ${page}
   click send cost      ${page}
   send cost            ${page}        ${cost}
   click notify user    ${page}
   click user id        ${page}
   close_notify         ${page}
   click notify ch      ${page}
   click sel ch         ${page}
   close_notify         ${page}
   click create         ${page}
   click edit           ${page}
   click cancel         ${page}
   click delete         ${page}
   click d cancel       ${page}
   click search         ${page}
   enter to search      ${page}         ${search}
   click alert download  ${page}
   click_alert_ui_setting    ${page}

# ----- Integration Related Helper ----- #
Integration.Get Data from integration
   ${page}      get page handle
   [Arguments]      ${i_name}       ${desc}         ${address}          ${integration}
   click integration menu  ${page}
   click integration admin        ${page}
   click integration module    ${page}
   click integration help      ${page}
   click create integration    ${page}
   click integration name           ${page}
   fill integration name            ${page}         ${i_name}
   click integration desc       ${page}
   fill integration desc       ${page}         ${desc}
   click app   ${page}
   select slack          ${page}
   click type  ${page}
   select webhook           ${page}
   click address    ${page}
   fill address    ${page}   ${address}
   click i create       ${page}
   click edit integration   ${page}
   click cancel edit integration    ${page}
   click delete integration         ${page}
   click cancel delete integration      ${page}
   click integration search         ${page}
   fill integration search          ${page}         ${integration}
   click integration download       ${page}
   click integration ui setting     ${page}


# -----SSO Related Helper ----- #
SSO.Perform action on SSO
   ${page}  get page handle
   click sso menu     ${page}
   click sso admin    ${page}
   click sso button   ${page}
   click sso help     ${page}
   click sso edit     ${page}
   click sso cancel   ${page}
   click sso delete   ${page}
   click sso delete no   ${page}

# -----API Related Helper ----- #
API.Perform action on API
   ${page}  get page handle
   click api menu     ${page}
   click api admin    ${page}
   click api button   ${page}
   click api help     ${page}

# -----Cost Related Helper ----- #
Costs.Perform action on Costs
   ${page}  get page handle
   [Arguments]       ${c_b_name}    ${c_b_desc}    ${c_s_name}     ${c_s_desc}    ${service}
   click c menu      ${page}
   click cost            ${page}
   click cost help       ${page}
   click cost share     ${page}
   click cost bookmark     ${page}
   enter cost b name       ${page}      ${c_b_name}
   enter cost b desc        ${page}     ${c_b_desc}
   select_cost_b_user       ${page}
   cost_b_user              ${page}
   cost_b_fav               ${page}
   cost_b_create            ${page}
   click cost subscription     ${page}
   enter cost sub name       ${page}         ${c_s_name}
   enter cost sub desc       ${page}         ${c_s_desc}
   create cost subscription      ${page}
   click cost screenshot     ${page}
   click cost filter     ${page}
   select cost usage filter      ${page}
   select cost cloudwiz      ${page}
   apply cost usage filter       ${page}
   click cost info     ${page}
   click cost reload     ${page}
   enter cost search     ${page}     ${service}
   click cost download   ${page}
   click cost ui setting    ${page}

# -----Resource Related Helper ----- #
Resources.Perform action on Resource
   ${page}  get page handle
   [Arguments]      ${res}
   click resource menu       ${page}
   click resource            ${page}
   click resource help       ${page}
   click resource search     ${page}
   enter resource search     ${page}     ${res}
   click resource download   ${page}
   click resource ui setting    ${page}

# -----Saving Related Helper ----- #
Savings.Perform action on Savings
   ${page}  get page handle
   [Arguments]      ${policy}
   click savings menu      ${page}
   click savings            ${page}
   click savings help       ${page}
   click savings search     ${page}
   enter savings search     ${page}     ${policy}
   click savings download   ${page}
   click savings ui setting   ${page}

# -----Compliance Related Helper ----- #
Compliance.Perform action on Compliance
   ${page}  get page handle
   [Arguments]      ${policy}
   click compliance menu      ${page}
   click compliance           ${page}
   click compliance help       ${page}
   click compliance search     ${page}
   enter compliance search     ${page}     ${policy}
   click compliance download   ${page}
   click compliance ui setting   ${page}

# -----Security Related Helper ----- #
Security.Perform action on Security
   ${page}  get page handle
   [Arguments]      ${policy}
   click security menu      ${page}
   click security           ${page}
   click security help       ${page}
   click security search     ${page}
   enter security search     ${page}     ${policy}
   click security download   ${page}
   click security ui setting   ${page}

# -----Utilization Related Helper ----- #
Utilization.Perform action on Utilization
   ${page}  get page handle
   [Arguments]      ${ser_name}
   click utilization menu      ${page}
   click ri button              ${page}
   click utilization           ${page}
   click utilization help       ${page}
   click utilization search     ${page}
   enter utilization search     ${page}     ${ser_name}
   click utilization download   ${page}
   click utilization ui setting   ${page}

# -----Coverage Related Helper ----- #
Coverage.Perform action on Coverage
   ${page}  get page handle
   [Arguments]      ${platform}
   click coverage menu     ${page}
   click ri       ${page}
   click on coverage button    ${page}
   click coverage help       ${page}
   click coverage search     ${page}
   enter coverage search     ${page}     ${platform}
   click coverage download   ${page}
   click coverage ui setting   ${page}