"""Manual testing:
--------------

Module 1:Testing concepts(Theory)what?
Module 2:Testing Project(Pratical)how?
Module 3:Agile Process - jira

Software:
A Software is a collection of computer programs that helps us to perform a task.

Types of Software:

1. System Software
Ex:Device drivers,oprating Systems, Servers, Utilites, etc.

2.Programming software
Ex: Compilers,deduggers,interpreters,etc.

3.Application software
Ex:Web Applications,Mobiles Apps,Desktop Applications etc.

X Bank(company)----------->IT Company -->Develop---->Test---->Deliver--->XBank

What is software Testing?
------------------------
Software Testing is a part of software development process.
Software Testing is an Activity to detect and identity the defects in the software.
The objective of testing is to quality product to the client

Software Quality:
1. Bug-Free
2. Delivered on time
3. With in Budget
4. Meets requirements and/or expections
5. Maintainable

Project Vs Product:
------------------
Project:
--------
If software application is developed for specific customer based on the requirement
then it is called Project.

Product:
-------
If software applications is developed for multiple customer based on market requirements
 then it called Product.

Error,Bug/defect & Failure
Error means human mistake (or) incorrect human action
Bug/defect application error
Failure means end user action

Why the software has bugs?

1. Miscommunication or no communication
2. Software complexity
3. Programming errors
4. Chaning requirements
5. Lack of skilled testers

***SDLC--Soft Development Life Cycle:
---------------------------------

Software Development Life Cycle is a process used by software industry to
design,develop and test software's.
1. P-People
2. P-Process
3. P-Product

SDLC--Soft Development Life Cycle:
1.Requirements Analysis
2.Design
3.Development
4.Testing
5.Maintenance

***Ex:Waterfall Model:(Liner Model):
-------------------------------
1.Requirements Analysis
2.System Design
3.Implementation
4.Testing
5.Deployment
6.Maintenance

Advantages of Waterfall Model:
-----------------------------
1.quality of the product will be good. (It means every stage to maintain detail Documentation).
2.Since Requirements changes are not allowed,chances of finding dugs will be less.
3.Initial inverstment is less since the testers are hired at the later stages.
4.Perferred for small projects where requirements are feezed.
(It means we can't modifly the Documentation)
5.Waterfall Model is using long time Projects.

Disadvantages of water model:
----------------------------
1.Requirements changes are not allowed.
2.If there is defect in Requirement that will be continued in later phases.
3.Total investment is more because time taking for rework on defect is time
consuming which leads to high investment.
4.Testing will start only after coding.

***Spiral Model:
------------
                                                 .
                                                 .
                   Planning                      .          Risk Analysis
                                                 .
                     (Requirement Analysis)      .
                                                 .
                                                 . Proto type
                                                 .
                     ...........................................................                                   .
                                                 .
                             cost                . Development & Testing
                                                 .
                           Customer Evaluation   .
                                                 .
                   (Testing)                     .                 Engineering & Execution
                                                 .
                           Evaluation            .
                                                 .
Spiral Model:
------------
1.Spiral Model is iterative model or repeated model and also version control model
2.Sprial Model overcome drawbacks of Waterfall Model.
3.We follow sprial model whenever there is dependency on the modules.
4.In every cycle new software will be relesed to customer.
5.Software will be released in multiple versions.So it is also called version control model.
6. This testing is used product based companies

Advantages of Spiral Model:
--------------------------
1.Testing is done in every cycle, before going to the next cycle.
2.Customer will get to use the software for every module.
3.Requirement changes are allowed after every cycle before going to the next cycle.


Disadvantages of Spiral Model:
-----------------------------
1.Reqirement changes are NOT allowed in between the cycle.
2.Every cycle of spiral model looks like waterfalls models.
3.There is no testing in requirement & design phase.

Proto Type--bule print of the software.
Initial Requirements from the customer-->Prototype--->Customer--->desing,coding,testing.

Ex:Gmail:
--------
Login
Inbox
Compose
sent
recive email
etc...

Banking:
-------
Login
Check balance
Fund transfer
Req statement
Add payee
etc...

***V Model:(OR) VV & Verification and Validation Model:
---------------------------------------------------
(business requriment specification & customer & user)
             Verification                         Validation
             (BRS/CRS/URS)------------------------(User Acceptance Testing)

             (Review)                             Black Box
                                                  Testing
                                                  Technique
(software requirement specifications)
             (SRS)--------------------------------(System Testing)

(high level design document)
             HLD---------------------

          Review                                 Integration Testing
(low level design document)
             LLD's-------------------



                                                White Box testing Technique

         Coding-----------------------------------(Unit Testing)


Static testing:
---------------
Testing the project related documents is called  as static testing.

(Document testing models)
1.Review
2.Walkthrough
3.Inspection

Dynamic testing:
---------------
Testing the actual software.

1.Unit testing.(Testing the single module is called as unit testing
or single component in our software)

2.Integration.

3.System testing.
4.UAT(User Acceptance Test)


***VV Model (or) Verification/Validation:
-------------------------------------
Verification:
------------
1.Verification checks whether we are building the right Product.
2.Focus on Documentation.
3.Verification typically involes.
4.Reviews.
5.Walkthroughs.
6.Inspections.

Validations:
-----------
1.Validation checks whether we are building the product right.
2.Takes place after verification are completed.
3.Focus on software.
4.Validation typically involves actual testing.
5.Unit testing, integration, System testing,UATTesting.


S1----S2----S3-------->Application.

Advantages:
----------
1.Testing is involved in each and every phase.

Disadvantages:
-------------
1.Documentation is more.
2.Initial Inverstment is more.

***Static testing techinques:
-------------------------
1.Review.
2.Walkthrough.
3.Inspection.

***Dynamic testing techinques:
--------------------------
1.Unit testing.
2.Integration testing.
3.System testing.
4.UAT

Review:
------
Conducts on documents to ensure correctness and completeness.

1.Requirements Reviews.
2.Design Reviews.
3.Test plan Reviews.
4.Test cases reviews etc.

Walkthrough:
-----------
1.It is a informal review.
2.Author reads the documents or code and discuss with peers.
3.Its not pre-planned and can be done whenever required.
4.Aslo walkthrough does not have minutes of the meet.

Inspection:
----------
1.Its amost formal review type.

2.In which at least 3-8 people will sit in the meeting
 1-reader 2-writer 3-moderator plus concerned.

3.Inspection will have a proper schedule which wii be
intimated via email to the concerned developer/tester.

***(QA Vs QC):(Quality Assurance & Quality control):
---------------------------------------------
QA is Process related.
QC is the actual testing of the software.

QA focuses on building in quality.
QC focuses on testing for quality.

QA is preventing defects.
QC is detecting defects.

QA is process oriented.
QC is Product oriented.

QA for entire life cycle.
QC for testing part in SDLC.

QE----> Quality Engineering

p-people.QC(Testers)
p-process.--(QA)
p-product.

Software Enginner/SE
Quality Engineer

***Levels of Testing:
-----------------
1.Unit Testing.
2.Integration Testing.
3.System Testing.
4.User Acceptance Testing(UAT).

Unit Testing:
------------
1.A unit is a single component or module of a software.
2.Unit testing conducts  on a single program or single module.
3.Unit testing  is white box testing technique.
4.Unit testing is conducted by the developers.

Unit Testing Techniques:
-----------------------
1.Basis path testing.(each and every line executed at one time)
2.Control structure testing.
3.Conditional coverage. (verify the conditions)
4.Loops Coverage.
5.Mutation testing.

Ex: Conditional coverage:
----------------------                   --

 a = 20
 b = 30
if a > b:
 print ("a is largest")
else:
("b is largest")

Ex:Loops Coverage:
-----------------

1.....5 numbers
i = 1
max = 10
  while(i<= max)
{
print (i)
i = i+1

}

Ex:Mutation testing:
-------------------

if user = 'scoft' and password = '123'
    allow login
else
 Not allow login

Integration Testing:5-------------------
1.Integration testing performed between 2 or more modules.
2.Integration testing focuses on checking data communication between multiple modules.
3.Integration testing is white box testing technique.

Types of Integration testing:
----------------------------
1.Incremental integration testing.
2.Non-incremental Integration testing.


Incremental integration testing:
-------------------------------
Incrementally adding the modules and modules and testing the data flow between the modules.

2 Approaches:
------------

Top Down--Incremental integration testing:
-----------------------------------------
Incrementally addingthe modules and testing the data flow between the modules.
And Ensure the module added is the child of previous module.



Bottom Up--Incremental integration testing:
-----------------------------------------
Incrementally addingthe modules and testing the data flow between the modules.
And Ensure the module added is the parent of previous module.


Sandwich/Hybrid Approach Testing:
--------------------------------
Combination of Top-Down & Bottom Up approach is called Sandwich Approach.


Non-Incremental Integration testing:
-----------------------------------
Adding all the modules in a sigle shot and test the data flow between modules.

Drawbacks:
---------
1.We might data flow between some of the modules.
2.If you find any defect we cant understand the root cause of defect.
------------------------------------------------------------------------------

8-12-21

System Testing:
--------------
1.Testing over all functionality of the application with respective client requirements.
2.It is a black box testing technique.
3.This testing is conducted by testing team.
4.After completion of component and integration level testing's we start system testing.
5.Before conducting system testing we should know the customer requirements.

System Testing focusses on below aspects:
----------------------------------------
1.User interface Testing.
2.Functional Testing.
3.Non-Functional Testing.
4.Usability Testing.

User accpectance testing:
-------------------------
After completion of system testing UAT team  conducts acceptance  testing in two levels.
1.Alpha testing.
2.Beta testing.

System Testing Types:
--------------------
1.GUI Testing.
2.Usability Testing.
3.Functional Testing.
4.Non - Functional Testing.


GUI Testing:
-----------
1.Graphical User-interface Testing or GUI testing is a process
 of testing the user interface of an application.

2.A graphical user interface includes all the elements such
as means,checkbox,buttons,colors,fonts,sizes,icons,content,and images.


GUI Testing Checklist:
---------------------
1.Testing the size,position,width,height of the elements.
2.Testing of the error messages that are getting displayed.
3.Testing  the different sections of the screen.
4.Testing of the font whether it is readable or not.
5.Testing of the screen in different resolutions with the help of zooming in and zooming out.
6.Testing the alignment of the texts and other elements like icons,buttons, etc,are in proper place or not.
7.Testing the colors of the fonts.
8.Testing whether the image has good clarity or not.
9.Testing the alignment of the images.
10.Testing of the spelling.
11.The user must not get frusted while using the system interface.
12.Testing whether the interface is attractive or not.
13.Testing of the scrollbars according to the size of the page if any.
14.Testing of the disabled fields if any.
15.Testing of the size of the images.
16.Testing of the heading whether it is properly aligned or not.
17.Testing of the color of the hyperlink.
18.Testing UI elements like button,textbox,textarea,checkbox,radio buttons,drop downs,links etc.

Usability Testing:
-----------------
1.During this testing validates application provided context
sensitive help or not to the user.

2.Checks how easily the end users are able to understand and
operate the application is called usability testing.


Functions Testing:
-----------------
1.Functions is nothing but behavior of application.

2.Function testing talks about how your feature should work.

Function Testing Cases:
----------------------
1.Object Properties Testing.
2.Database Testing.
3.Error Handling.
4.Calculation/Manipulations Testing.
5.Links Existence & Links Execution.
6.Cookies & Sessions.

Functionality Testing:
---------------------
Object Properties Testing:
-------------------------
Check the properties of objects present on the application.
Ex: Enable,Disable,Visible,Focus.....

Datebase Testig/Backend testing:
-------------------------------
DML operations (Data Manipulation Language).
1.insert.
2.update.
3.delete.
4.select.

1.Table & Column level validations( Column type,Column length,numbers of Columns...).
2.Relation between the tables (Normalization).
3.Functions.
4.Procedures.
5.Triggers.
6.Indexes.
7.Views.
8.etc...

Error Handing Testing:
---------------------
1.Tester verify the error messages while performing incorrect actions on the application.
2.Error messages should be readle.
3.User understand/Simple language.

Incorrect data.
Invalid User.

Calculation/Manipulation testing:
--------------------------------
Tester should verify the calculations.

Links:
-----
where exactly the links are placed ---- Links existence.
Links are navigating to proper page or not ----- links execution.

1.Internal links.(click the link can navigate the same page to jump the another section)
2.External links.(click the link can navigate next page)
3.Brokens links.(click the link cannot be navigate any other page)

Cookies:
-------
1.Temporary files created by browser while browsing the pages through internet.

2.Sessions are time slots created by the server.
Sessions will be expired after some time (If you are idle for some time).

Non-Functions Testing:
---------------------
1.Once the application functionality is stable then we do Non - Functional testing.
2.Focus on performance,load it can take and security etc.

Non-Function testing Topics:
---------------------------
1.Load.
2.Stress.
3.Volume.

Load: Gradaully Increasing the load on the application  slowly then check the speed on the application.
Stress:Suddenly increase/decrease the load on the application and check speed of the application.
Volume:Check how much data is able to handle by the application.

Security testing: How secure our application.
----------------

Authentication-----> Users are valid or not.

Autherization/Access Control-----> Permissions of the valid user.


Recovery testing:
----------------
Check the system change to abnormal to normal.

Compatibility testing:
---------------------
1.Forward Compatibility.
2.Backward Compatibility.
3.Hardware Compatibility.(configuration testing)

Installing testing:
------------------
1.Check screen are clear to understand.
2.Screen navigation.
3.Simple or not.
4.Un-installation.

Sanitation/Garbage testing:
--------------------------
If any application provides extra features/functionality then we consider them as bug.


Difference between Functional Testing Vs Non-Functional Testing:
---------------------------------------------------------------

Functional Testing:
------------------
1.Validates functionality of software.
2.Functionality describes what software does.
3.Concentrates on user requirement.
4.Functional testing takes place before Non-functional testing.

Non-Functional Testing:
----------------------
1.Verify the performance,security,reliability of the software.
2.Non-functionality describes how to software works.
3.Concentrates on user expection.
4.Non-functional testing performed after finishing functional testing.


Testing Technologyes:
--------------------
***Regression Testing:
---------------------
1.Testing conducts on modified build to make sure there will not be impact on existing functionality because of changes like adding/deleting/modifying features.

Types of Regression:
-------------------

Unit Regression Testing:
-----------------------
1.Testing only the change/modification done by the developer.

Regional Regression Testing:
---------------------------
1.Testing the modified module along with the impacted modules.
2.Impact Analysis meeting conducts to identify impacted modules with QA & Dev.

Full Regression:
---------------
1.Testing the main feature & remaining part of the application.
2.Ex:Dev has done changes in many modules, instead of identifying impacted modules,we perform one round of full regression.

Re-Testing:
----------
1.Whenever the developer fixed a bug,tester will test the bug fix is called Re-testing.
2.Tester close the bug if it worked otherwise re-open and send to de
3.To ensure that the defects which were found and posted in the earlier build were fixed or not in the current build.

Example:
1.Build 1.0 was released. Test team found some defects (Defect id 1.0.1,1.0.2)and posted.
2.Build 1.1 was released,now testing the defects 1.0.1 and 1.0.2 in this build is re-testing


Example: Re-Testing Vs Regression Testing:
-----------------------------------------
1.An Application under test has three modules namely Admin ,Purchase and Finance.
2.Finance module depends on purchase module.
3.If a tester found a bug on purchase module and posted. Once the bug is fixed,the tester
needsto do Retesting to verify whether the bug related to the purchase is fixed or not and
also tester needs to do Regression Testing to test the finance module which depends on
the purchase module.

Smoke Testing:(Build verification testing):
-----------------------------------------

--->Smoke and Sanity Testing come into the picture after build release.

1.Smoke test is done to make sure the build we received from the
  development team is testable/stable.(installing issues)
2.Smoke testing is performed by both Developers and testers.
3.Smoke testing bulid may be either stable or unstable.
4.It is done on intial builds.
5.It is a part of basic testing.
6.Usually it is done every time there is a new build release.


Sanity Testing:
--------------
1.Sanity test is done during the release phase to check for the
  main functionalities of the application without going tester.
2.Sanity testing is performed by testers alone.
3.Sanity testing, build is relatively stable.
4.It is done on stable builds.
5.It is s part of regression testing.
6.it is planned when there is no enough time to do in depth testing.

Exploratory Testing:
-------------------
1.We have to explore the application , understand completely and test it.
2.Understand the appliation, identity all possible scenarios, document it then use it for testing.
3.We do exploratory testing when the application ready but there is no requirement.
4.Test engineer will do exploratory testing when there is no requirement.

Draw backs:
----------
1.You might misunderstand any feature  as a bug (or) any bug as a feature since you do not have requirement.
2.Time consuming.
3.If there is any bug in application , you will never know about it.


Adhoc Testing:
-------------
1.Testing application randomly without any test cases or any business requirement document.
2.Adhoc testing is an informal testing type with an aim to break the system.
3.Tester should have knowledge of application even thou he does't have requirements/test cases.
4.This testing is usually an unplanned activity.

Ad Hoc Testing cases:
--------------------
1.No Documentation.
2.No test Design.
3.No test case.

Monkey/Gorilla Testing:
----------------------
1.Testing application randomly without any test cases or any business requirement document.
2.Adhoc testing  is an informal testing type with an aim to break the system.
3.Tester do not have knowledge of application.
4.Suitable for gaming applications.

Adhoc Testing Vs Monkey Testing Vs Exploratory Testing:
------------------------------------------------------

Adhoc Testing:
-------------
1.No documentation.
2.No plan.
3.Informal testing.
4.Testing should know application functionality.
5.Random Testing.
6.Intension is to break the application / find out corner defects.
7.Any applications

Monkey Testing:
--------------
1.No documentation.
2.No plan.
3.Informal testing.
4.Testing doesn't know application functionality.
5.Random Testing.
6.Intension is to break the application / find out corner defects.
7.Gaming applications

Exploratory Testing:
-------------------
1.No documentation.
2.No plan.
3.Informal testing.
4.Testing doesn't know application functionality.
5.Random Testing.
6.Intension is to learn or explore functionality of application.
7.Any application which is new to tester.

Positive Testing:
----------------
1.Testing the application with valid inputs is called as positive Testing.
2.It checks whether an application behaves as expected with positive inputs.
Ex:
--
Enter Only Numbers :
99999
Positive Testing
3.There is a text box in an application which can accpet only numbers.
4.Entering values up to 99999 wii be acceptable by the system and any other values apart from this should not be acceptable.
5.To do positive testing set the vaild input values from 0 to 99999 and check whether   the system is acceptance  the values.

Negative Testing:
----------------
1.Testing the application with  invalid inputs is called as negative testing.
2.It checks whether an application behaves as expected with the negative inputs.
EX:
--
Enter Only Numbers:
abcdef
Negative Testing
3.Negative testing can be performed by entering characters A to Z or from a to z either  software system should throw an error message  for these invalid data inputs.

Positive V/s Negative Test Cases:
--------------------------------
Requirement:
-----------
1.For example if a text box is listed as a feature and in FRS it is mentioned as textbox accepts 6-20 characters and ony alphabets.

Positive Test cases:
-------------------
1.Textbox accepts 6 characters.
2.Textbox accepts upto 20 chars length.
3.Textbox accepts any value in between 6-20 chars length.
4.Textbox accepts all alphabets.

Negative Test Cases:
-------------------
1.Textbox should not accept less than 6 chars.
2.Textbox should not accept chars more than 20 chars.
3.Textbox should not accept special characters.
4.Textbox should not accept numerical.

END-To- END Testing:
-------------------
1.Testing the overall functionalities of the system including the data integration  among all the modules is called end-to-end testing.

End -To-Testing Test Cases:
--------------------------
1.Login.
2.Add New Customer.
3.Edit customer.
4.Delete customer.
5.Logout.

Globalization and Localization Testing:
--------------------------------------

Globalization Testing:
---------------------
1.Performed to ensure the system or software application can run in any cultural or local environment.
2.Different aspects of the software application are tested to ensure that it supports every language and different attributes.
3.It tests the different currency formats, mobiles numbers formats and address formats are supported by the application.
4.For example,Facebook.com  supports many of the languages and it can be accessed by people of different countries .hence it is a globalized product.

Localization Testing:
--------------------
1.Performed to check system or software application for a specific geographical and cultural environment.
2.Localized product only supports the specific  kind of language and is usable only in specific region.
3.It testes the specific currency format,mobiles number format is working properly or not .
4.For Example, baidu.com supports only the chinese language and can be accessed only by people of few countries. hence it is a localized product.

Test Design techniques/Test Data Design Techniques/Test:
-------------------------------------------------------
 case Design Techniques:
 ----------------------
 1.Used to perpare data for testing.

 1.Reduce the data.
 2.More Coverage.


Test Design techniques:
----------------------
1.Test design techniques helps to design better cases.
2.Reduce the number of test cases to be executed.

Techniques:
----------
1.Equivalence class partitioning.
2.Boundary value Analysis(BVA).
3.Decision table based testing.
4.state transition.
5.Error Guessing.

Equivalence Class Partition (ECP):
--------------------------------

Value check
Clasify/devide/partition the data in to multiple classes.

1.Partition data into various classes and we can select data according to class then test.

2.It  reduce the number of test-cases and saves time for testing.

Enter the Number:
Allow digits from 1-500

Equivalence Class Partition (ECP):
---------------------------------
Enter the Name:

Allows only alphabets.

Divided values into Equivalence Classes:
---------------------------------------
1.A.Z----->(valid).
2.a.z----->(valid).
3.Special Characters------>(invalid).
4.Spaces----->250(invalid).
5.Numbers----->320(invalid).

Boundary Value Analysis(BVA):
----------------------------

Boundary of the values.

Min
Min+1
Min-1

Max
Max+1
Max-1




1.BVA technique used to check boundaries of the input.

Example:
-------
Enter a age:

Allows digits from 18 - 35.

Input Domain Testing:
--------------------
The value will be verified in the text  box/input fields.
We use ECP & BVA techniques.


Decision Table:
--------------

If we have more number of constions / actions then we use decision table technique.

1.Decision table is also called as Cause-Effect table.
2.This technique will be used if we have more conditions and corresponding actions.
3.In decision table technique, we deal with combinations of inputs.
4.To identify the test cases with decision table,we consider conditions and actions.

Desicion Table Example:
----------------------
1.Take an example of transferring money online to an  account which is already added and approved.

Here the condition to transfer money are:
----------------------------------------
1.Account already approved.
2.OTP(one time passward)matched.
3.Sufficient money in the account.

And the actions performed are:
-----------------------------
1.Transfer money.
2.Show a message as insufficient amount.
3.Block the transaction incase of suspicious transaction.

State Transition:
----------------
1.In state transition technique changes in input conditions change the state of the application.
2.This testing technique allows the tester to test the behaviour of an AUT.
3.The tester can perform this action by entering various input conditions in a sequence.
4.In state transition technique, the testing team provides postive as well as negative input test values for evaluating the system behaviour.

State Transition Example:
------------------------
1.Take an example of login page of an application  which locks the user name after three wrong attempts of passward.

1.First Attempt,Second Attempt,Third Attempt.
2.Home page.
3.Display a message as "Account Locked, please consult Administrator".

Error Guessing:
--------------
1.Error guessing is one of the testing techniques used to find bugs in a sotfware application based on testers pripor experience.
2.In Error guessing we don't follow any specific rules.
3.It depends on tester analytical skills and experience.
4.Some of the examples are:
---->Submitting a from without entering values.
---->Entering invalid values such as entering alphabets in the numeric field.

SDLC-SOFTWARE DEVELOPMENT LIFE CYCLE:
------------------------------------
ReqAnalysis,Desing,Testing,Deployment,Maintance.


STLC--SOFTWARE TESTING LIFE CYCLE:
-----------------------------
 1.Requirement Analysis.
 2.Testing Planning.
 3.Testing Desing.
 4.Test Execution.
 5.Defect /Bug Reporting & Tracking.
 6.Test Closure.

 Software Testing Life Cycle(STLC) Steps:
 ---------------------------------------
 1.Requirement Analysis.
 2.Testing Planning.
 3.Test Case Development.
 4.Environment Setup.
 5.Test Execution.
 6.Test Cycle Closure.

-------------------------------------------------------------------------------------------------------------------------

Explanation of STLC:
-------------------
1.Testing:
---------

Input:
-----
1.Project plan.
2.Funtional Requirements

Activities:
----------
1.Identify the resources.
2.Team formation.
3.Test estimation.
4.Preparation of test plan.
5.Reviews of test plan.
6.Test plan sign-off.

Responsiblity:
------------
1.Test Lead/Team Lead(70%)
2.Test Manger(30%).

Out Come:
--------
1.Test plan Document.

------------------------------------------------------------------------------------------------------------------------

2.Test Designing:
----------------

Input:
-----
1.Project plan.
2.Funtional Requirements.
3.Test plan.
4.Design Docs.
5.Use cases.

Activities:
----------
1.preparation of test Scenarios.
2.Preparation of test cases.
3.Reviews on test cases.
4.Traceability Matrix.
5.Test cases sign-off.


Responsiblity:
------------
1.Test Lead/Team Lead(30%).
2.Test engineer(70%).

Out Come:
--------
1.Test Cases Document.
2.Traceability Matrix.

-------------------------------------------------------------------------------------------------------------------------

3.Test Execution:
----------------
Input:
-----
1.Functional requirements.
2.Test plan.
3.Test cases
4.Build from development team.

Activities:
----------
1.Executing test cases.
2.prepartion of test report/test log
3.identifying defects.


Responsiblity:
------------
1.Test Lead/Team Lead(10%).
2.Test engineer(90%).

Out Come:
--------
1.Status/test reports.

-------------------------------------------------------------------------------------------------------------------------

4.Defect Reporting & Tracking:
-----------------------------

Input:
-----
1.Test cases.
2.Test reports/test log.


Activities:
----------
1.Preparation of defect report.
2.Reporting defects to developers.


Responsiblity:
------------
1.Test Lead/Team Lead(10%).
2.Test engineer(90%).

Out Come:
--------
1.Defect report.

------------------------------------------------------------------------------------------------------------------------

5.Test Closure/Sign-Off:
-----------------------

Input:
-----
1.Test reports.
2.Defects reports.

Activities:
----------
1.Analyzing test reports.
2.Analyzing bug reporting.
3.Evaluating exit criteria.

Responsibility:
--------------
1.Test Lead/Team Lead(70%).
2.Test engineer(30%).

Out Come:
--------
1.Test Summary reports.

-------------------------------------------------------------------------------------------------------------------------

Test Plan Contents:
------------------
1.A test plan is a document that describes the test scope, test strategy,objectives,schedule,deliverables and resources required to perform testing for a software product.

Test Plan Template Contents:
---------------------------
1.Overview.
2.Scope
  a)Inclusions.
  b)Test environmens.
  c)Exclusions.
3.Test Strategy.
4.Defect Reporting Procedure.
5.Roles/Responsibilities.
6.Test Schedule.
7.Test Deliverables
8.Pricing.
9.Entry and exit criteria.
10.Suspension and resumption criteria.
11.Tools.
12.Risks and mitigations.
13.Approvals.

Use Case ,Test Scenario & Test Case:
-----------------------------------
1.Use case describes the requirement.
2.Use case contains three itmes
  a)Actor,which is the user,which can be a single person or a group of people ,interacting with a process.
  b)Action,whichis to reach the final outcome.
  c)Goal/outcome,which is the succssful user outcome.

Test Scenario:
-------------
1.A possible area to be tested (what to test).

Test Case:
---------
1.Step by step actions to be performed to validate functionality of AUT(how to test).
2.Test case contains test steps, expected result & actual result.

Sample Use Case:
---------------
Example:
-------

Library User----->Register book loan----->Register book return------->Query book availability----->Librarian------->Add new book.


 Use Case V/s Test Case:
 ----------------------
 1.Use Case---->Describes functional requirement,prepared by business analyst(BA).

 2.Test Case----->Describes test steps/procedure,prepared by test engineer.


Test Scenario V/s Test Case:
---------------------------
1.Test Scenario is "What to be tested" and test case is "How to be tested".

Example:
-------
1.Test Scenario:---->Checking the functionality of login button.
  a)TC1:Click the button without entering user name and password.
  b)TC2:Click the button only entering user name.
  c)TC3:Click the button while entering wrong user name and wrong passward.

Test Suite:
----------
1.Test suite is group of test  cases which belongs to same category.

What is Test Case:
-----------------
1.A Test case is a set of actions executed to validate particular feature or functionality of your software application.

Test Case Contents:
------------------
1.Test case id.
2.Test case title.
3.Description.
4.Pre-condition.
5.Priority(P0,P1,P2,P3)----order.
6.Requirement id.
7.Steps/actions.
8.Exected result.
9.Actual result.
10.Test data.

Requirement Traceability Matric(RTM):
------------------------------------

What is RTM (Requirement Traceability Matrix):
1.RTM describes the mapping of requirement's with the test cases.
2.The main purpose of RTM is to see that all test cases are covered so that no functionality should miss while doing software testing.

Requirement Traceability Matrix--Parameters Include:
---------------------------------------------------
1.Requirement ID.
2.Req Description.
3.Test case ID's.

Sample RTM:
----------

1.REQ NO:
--------
 a)123.
 b)345.
 c)456.

2.REQ DESC:
----------
 a)Login to application.
 b)Ticket Creation.
 c)Search Ticket.

3.TESTCASE ID:
-------------
 a)TC01,TC02,TC03

4.STATUS:
--------
  a)pass.
  b)fail.

Test Environment:
----------------
1.Test Environment is a platform specially build for test case execution on the software product.
2.It is created by integrating the required software and hardware along with proper network configurations.
3.Test environment simulates production/real time environment.
4.Another name of test environment is test bed.









"""