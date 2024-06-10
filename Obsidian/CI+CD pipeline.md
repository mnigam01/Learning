developers push their code in a code repository, when any change is done in master branch code is build, tested on test cases provided and deployed. This process is called ci/cd pipeline.
it helps deployment testing fast. Hence it is preferred
![[Pasted image 20240529164921.png]]

Create 2 IAM roles

in aws search pane search for iam click it, in left pane click on roles, on right side click on create role.
select use case ec2 click next.
search for policy amazonec2roleforawscodedeploy
![[Pasted image 20240529205427.png]]

click on next.
give role name. Click on finish or create role.

For 2nd role click on create role.
in use case from drop down choose codeDeploy

![[Pasted image 20240529205625.png]]

click next. click next. give role name. and finish



**Create EC2 instance**

in search bar search ec2. click on launch instance. give instance a name. select ubuntu as os. select machine configuration from dropdown. select ubuntu server 20.04.


leave everything as it is. in key pair. create a new key pair. give key pair name. leave everything default and finish.

Allow http traffic from the internet.
click on launch instance.

Now need to attach newly created iam role to ec2 instance.

select instance and click on actions then go in security and modify iam role. choose an iam role. click on update iam role
![[Pasted image 20240529210311.png]] 

reboot the machine to allow changes to take affect.
![[Pasted image 20240529210457.png]] 

select server and click on connect
![[Pasted image 20240529210609.png]]