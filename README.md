# python-http
Elias Neypes & Vy Phan
Apex Legends HTTP server



Demo:
https://www.youtube.com/watch?v=g6l3LZFDMCE

1. Problem and relevancy: “Apex Legends” is an online multiplayer video game on various gaming platforms. Because it is a new game and very popular, players are seeking to be the best and need to distinguish themselves someway in their gameplay. This can be tracked by simply looking at players’ statistics. 
 
2. Solution Architecture:The Python Flask application will be developed locally where we then push our updated code to Github. This pushing event will then trigger JenkinsX where it will run a unit test for the code and push it to our WIP branch of our dev stage repository. We then have a pre-merge gating where we have to create a pull request for the new commit and have a chance to look at the proposed changes and merge with the master branch of the dev stage. This will then prompt Jenkins X to push the code to the staging repository where it will run through functional tests. After it passes, it will go to the production stage where the website might go through production tests before showing for visitors. 

3. Cloud services used:  Azure Kubernetes - Cluster for Jenkins X and our application to run on 
Azure Container Registry - Stored our images 
GitHub - Code versioning and storage 
AWS EC2 - VM for command line for JenkinsX, Azure cloud services, code development

4. Lessons learned: Don’t delete anything you think might be useless. Azure does not warn you of dependencies and may not even ask for confirmation. Azure works well with its own environment (using Azure repositories, Pipelines, etc.). Azure has their own terminology for many things but is overall similar to other cloud services like AWS. Azure is very picky on “subscriptions” where it is a pay-as-you-go model for any services you try to use. This made it difficult for us to work together on the same project with different accounts. Even with full access permissions for both parties, we found ourselves still being limited. Jenkins X Serverless is still new (has plenty of bugs) and was not good to start with while learning its functions. 

5. Elias: Reaching out to the JenkinsX community about issues, initialized JenkinsX and the environments to work with. Provisioned a vm for both of us to develop on to use JenkinsX with. Created unit tests and configured JenkinsX pipeline to work with Git repositories. Debugged JenkinsX pipeline. 
Vy: Made the website’s front-end and back-end. Provisioned the Azure’s resources such as the Kubernetes Cluster and Container Registry necessary for JenkinsX to run on. Configured application and cloud services to interact with one another. Experimented with Azure Pipelines. 

7. References: https://www.reddit.com/r/apexlegends/comments/aoxw4z/apex_legends_api/
https://apex.tracker.gg/site-api https://github.com/jenkins-x/jx/issues/3697
https://jenkins.io/projects/jenkins-x/
https://www.youtube.com/watch?v=DmhDvr8fExA 
