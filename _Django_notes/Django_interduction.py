# Django
#----> web frame work
"""
Frame work:
Frameworks are software that is developed and used by developers to build applications

Best python frame works:
1 Bottle
2 Django
3 Giotto
4 pylons
5 cherry py

Web framework:
It is a software framework that is designed to support the development of web applications including
--->Web service
--->Web resources
--->web API'S

Django
Django is a free and open source web application framework written python
#named after famous guiterist Django Reinhardt
#created in 2003 open sourced in 2005

--->Adrian Holovaty and simon Willison
---->version 3.0

Features of Django
1 stability
2 Excellent Documentation
3 Resolves Security issues
4 Highly Scalable
5 Utilizes SEO(search engine optimization )
6 Huge Library of Packages

Django works:
MVT(architecture)
M--Model
V--View
T--Template

                                             user
                                              .
                                              .
                                              .
                                       view (Request Response)url links
                                        .                   .
                                        .                   .
                data base------------> model              template(html, css ,forms)

Django Supports
1 Object Relational Mapping
2 Multilingual Support
3 Web development with light weight web server

Django follows MVT architecture:

                        Http Request------------------- Urls(urls.py)
                                                          .
                                                          .
                                            Forward request to appropriate view
                                                          .
                                                          .
                                                          .
                                                          .
            model(models.py)--->read/write data------->views(views.py)----------->Http Response(Html)
                                                          .
                                                          .
                                                          .
                                                          .

                                            Template(filename.py)
Model:

model is going to act as the interface of your data.
It is responsible for maintaining data.
It is the logical data structure behind the entire application and is
represented by a database(generally relational databases such as MySql postgres

file:
model.py

View:

views act as a link between the model data and the templates.
It contains python logics which required to web app
This view also sends response to the user when the application is used to
understand briefly, we can say that this view.py can deal with HttpResponse

file:
view.py

Template:
A template consists of static parts of the desired HTML output as well as some special
syntax  describing
how dynamic content will be inserted

Contains:
Html,Css,Boostrap,Javascript
---------------------------------------------------------------------------------------------
Diagram:

  Model---------->.                    Template
                  .                     .
                  .    user input       .
                  .                     .
                                        .(Display data)
                  .
                  .(complete data)      .
(design & updation).
                  .                     .
                view------------------->

----------------------------------------------------------------------------------------------------------

Planing:
                                         Me
                                         .
                                         .
                                         .
                                     Browser
                                     .     .
                                           .
                                     .     .(urls)
                         (templates) .     .
                                     .     .
                                     .     .
                                     views
                                       .
                                       .
                                       .
                                       .
                                    models(orm)
                                       .
                                       .
                                       .
                                    Database

-------------------------------------------------------------------------------------------------------------
install Django:

1. Pip install virtualenv
2. Virtualenv filename
3. Open filename open
4. activate
5. Django-admin startproject project name


"""
