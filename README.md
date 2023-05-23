Hello KubeWorld!
This project is to learn more about kubernetes and how to use it for devsecops

Prerequisites
Before proceeding, ensure that you have the following prerequisites set up:

Docker installed on your local machine
Kubernetes cluster or access to a Kubernetes environment (MiniKube)
kubectl command-line tool configured to communicate with your Kubernetes cluster
Python 3 installed on your local machine
Deployment
To deploy the Selenium nodes in Kubernetes, follow these steps:

Clone or download this repository to your local machine.

Open a terminal and navigate to the repository's directory.

Ensure that you are logged in and connected to your Kubernetes cluster using the kubectl command-line tool.

Deploy the Selenium nodes by running the following command:

bash
Copy code
make deploy-selenium
This command will create a Kubernetes namespace called selenium (if it doesn't exist already) and deploy the Selenium hub, along with nodes for Chrome, Firefox, and Internet Explorer.

Test Execution
After successfully deploying the Selenium nodes, you can run the test scripts for each browser as follows:

Chrome: Execute the following command to run the Chrome test script:
bash
Copy code
make test-chrome
Firefox: Run the Firefox test script by executing the following command:
bash
Copy code
make test-firefox
Internet Explorer: Execute the following command to run the Internet Explorer test script:
bash
Copy code
make test-ie
Each test script will open a website and print the page title.


That's it! You should now be able to deploy Selenium nodes in Kubernetes, run the test scripts for different browsers, and manage the Python dependencies using the provided Makefile. Feel free to customize the setup based on your specific needs. Happy testing!
