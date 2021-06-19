A Take Home Project

This a Vulnerable web application demonstrating how input fields are vulnerable to sql injections. 

The added security measures are parameterized queries and a WAF particularly (Mod-Security) wich is integrated with the apache webserver.


Steps to set up the environment: 
Python-Flask to build the web-application, MySQL to set up a dummy database. 
Apache web server 
AWS Cloud (EC2 - Ubuntu)
Modsecurity - WAF

Project Details:
The application is vulnerable to an SQL injection; however, the ramifications of this vulnerability are limited. Because the application only matches the username using the SQL query (not the username and the password) we can only bypass the username check. However, that does not mean this vulnerability is entirely useless to an attacker. Since the application gives no feedback on whether a username exists in the database it can be hard to bruteforce a user's password (because an attacker must bruteforce all possible usernames and passwords). If the attacker knew about the existence of this SQL injection they would be able to bypass the username check and only focus on performing a bruteforce attack for the password. This takes us from a O(m^n) complexity (where m is the size of the username search space and n is the size of the password search space) to a O(n) worst case complexity.



Research and references used: 
https://flask.palletsprojects.com/en/2.0.x/
https://www.codementor.io/@abhishake/minimal-apache-configuration-for-deploying-a-flask-app-ubuntu-18-04-phu50a7ft
https://coreruleset.org/installation/  
