# IC Project


![Visualization of the codebase](./diagram.svg)

```mermaid
---
title: PMO Input.xlsx
---
flowchart LR
    id;
    name

```
```mermaid
graph TD;
  PMO_Input -->|Contains| Project_Sheet
  PMO_Input -->|Contains| Details_Sheet
  PMO_Input -->|Contains| Funding_Sheet
  PMO_Input -->|Contains| Financials_Sheet
  Project_Sheet -->|Contains| tbl_PMO_Project
  Details_Sheet -->|Contains| tbl_PMO_Details
  Funding_Sheet -->|Contains| tbl_PMO_Funding
  tbl_PMO_Project -->|Has Field| Project_Creation_ID
  tbl_PMO_Project -->|Has Field| Workday_Project_ID
  tbl_PMO_Project -->|Has Field| Workday_Program_ID
  tbl_PMO_Project -->|Has Field| Project_ID
  tbl_PMO_Project -->|Has Field| Title
  tbl_PMO_Project -->|Has Field| Activity_Status
  tbl_PMO_Project -->|Has Field| Description
  tbl_PMO_Project -->|Has Field| Senior_PM
  tbl_PMO_Project -->|Has Field| Gate_Status
  tbl_PMO_Project -->|Has Field| Project_Manager
  tbl_PMO_Project -->|Has Field| Client
  tbl_PMO_Project -->|Has Field| Sponsor
  tbl_PMO_Project -->|Has Field| Planner
  tbl_PMO_Project -->|Has Field| SME_Required
  tbl_PMO_Project -->|Has Field| SME_Name
  tbl_PMO_Project -->|Has Field| Parent
  tbl_PMO_Project -->|Has Field| Child
  tbl_PMO_Project -->|Has Field| Location
  tbl_PMO_Project -->|Has Field| Facility_By_Code
  tbl_PMO_Project -->|Has Field| Address
  tbl_PMO_Project -->|Has Field| Building_Number
  tbl_PMO_Project -->|Has Field| Area/Room_Num
  tbl_PMO_Project -->|Has Field| Conventions_&_Reservations_Outdoor_Spaces
  tbl_PMO_Project -->|Has Field| Campus
  tbl_PMO_Project -->|Has Field| Summer_Sensitive
  tbl_PMO_Project -->|Has Field| Summer_Sensitive_Year
  tbl_PMO_Project -->|Has Field| Design_Completion_Deadline
  tbl_PMO_Project -->|Has Field| Project_Type
  tbl_PMO_Project -->|Has Field| Team
  tbl_PMO_Details -->|Has Field| Workday_Project_ID
  tbl_PMO_Details -->|Has Field| Workday_Program_ID
  tbl_PMO_Details -->|Has Field| Project_ID
  tbl_PMO_Details -->|Has Field| Activity_Status
  tbl_PMO_Details -->|Has Field| Title
  tbl_PMO_Details -->|Has Field| Project_Manager
  tbl_PMO_Details -->|Has Field| Fund_No
  tbl_PMO_Details -->|Has Field| Deliverable
  tbl_PMO_Details -->|Has Field| I&R
  tbl_PMO_Details -->|Has Field| Study
  tbl_PMO_Details -->|Has Field| Design
  tbl_PMO_Details -->|Has Field| Construction
  tbl_PMO_Details -->|Has Field| 23/24_Check
  tbl_PMO_Details -->|Has Field| 22/23_Check
  tbl_PMO_Details -->|Has Field| Close_Log
  tbl_PMO_Details -->|Has Field| BT_Close_Date
  tbl_PMO_Details -->|Has Field| BT_Creation_Date
  tbl_PMO_Details -->|Has Field| Report_Card_CFI
  tbl_PMO_Details -->|Has Field| Report_Card_FY
  tbl_PMO_Details -->|Has Field| Contact_Person
  tbl_PMO_Details -->|Has Field| SME_ARCH
  tbl_PMO_Details -->|Has Field| SME_MECH
  tbl_PMO_Details -->|Has Field| SME_ELEC
  tbl_PMO_Details -->|Has Field| Potential_Closeout_Date
  tbl_PMO_Funding -->|Has Field| Workday_Project_ID
  tbl_PMO_Funding -->|Has Field| Workday_Program_ID
  tbl_PMO_Funding -->|Has Field| Project_ID
  tbl_PMO_Funding -->|Has Field| Activity_Status
  tbl_PMO_Funding -->|Has Field| Title
  tbl_PMO_Funding -->|Has Field| Project_Manager
  tbl_PMO_Funding -->|Has Field| Fund_Name
  tbl_PMO_Funding -->|Has Field| Fund_No
  tbl_PMO_Funding -->|Has Field| GL_Account
  tbl_PMO_Funding -->|Has Field| Program
  tbl_PMO_Funding -->|Has Field| Sub-Program
  tbl_PMO_Funding -->|Has Field| Funding_Version
  tbl_PMO_Funding -->|Has Field| PAPI_22/23
  tbl_PMO_Funding -->|Has Field| PAPI_23/24
  tbl_PMO_Funding -->|Has Field| PAPI_24/25
  tbl_PMO_Funding -->|Has Field| PAPI_ID
  tbl_PMO_Funding -->|Has Field| CFI
  tbl_PMO_Funding -->|Has Field| CFI_No
  tbl_PMO_Funding -->|Has Field| FRP
  tbl_PMO_Funding -->|Has Field| QRT
  tbl_PMO_Funding -->|Has Field| Major_Project
  tbl_PMO_Funding -->|Has Field| Top_Shelf
  tbl_PMO_Funding -->|Has Field| Self_Funded
  tbl_PMO_Funding -->|Has Field| Multiyear_Funding
  tbl_PMO_WD_Financials -->|Has Field| Workday_Project_ID
  tbl_PMO_WD_Financials -->|Has Field| Workday_Program_ID
  tbl_PMO_WD_Financials -->|Has Field| Project_ID
  tbl_PMO_WD_Financials -->|Has Field| Activity_Status
  tbl_PMO_WD_Financials -->|Has Field| Title
  tbl_PMO_WD_Financials -->|Has Field| Project_Manager
  tbl_PMO_WD_Financials -->|Has Field| Budget
  tbl_PMO_WD_Financials -->|Has Field| Actuals
  tbl_PMO_WD_Financials -->|Has Field| Commitments
  tbl_PMO_WD_Financials -->|Has Field| Obligations
  tbl_PMO_WD_Financials -->|Has Field| Available_Budget
  tbl_PMO_WD_Financials -->|Has Field| Planner
```
