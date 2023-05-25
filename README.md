# Hello KubeSelenium!

This project is to learn more about kubernetes and how to use it for devsecops CI testing with Selenium!
Selenium is great for all kinds of fun so this hello world will be a good starting place to learn

# Prerequisites
Before proceeding, ensure that you have the following prerequisites set up:

- Docker installed on your local machine
- Kubernetes cluster or access to a Kubernetes environment (MiniKube)
- kubectl command-line tool configured to communicate with your Kubernetes cluster
- Python 3.7 or greater installed on your local machine

# Deployment
To deploy the Selenium nodes in Kubernetes, follow these steps:

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the repository's directory.

3. Ensure that you are logged in and connected to your Kubernetes cluster using the kubectl command-line tool.

# Deploy the Selenium nodes by running the following command:
make deploy-selenium
This command will create a Kubernetes namespace called selenium (if it doesn't exist already) and deploy a selenium cluster for common browsers (chrome, firefox, ie)

# Test Execution
After successfully deploying the Selenium nodes, you can run the test scripts for each browser as follows:

- Chrome: Execute the following command to run the Chrome test script:
make test-chrome
- Firefox: Run the Firefox test script by executing the following command:
make test-firefox
- Internet Explorer: Execute the following command to run the Internet Explorer test script:
make test-ie

Each test script will open a website and print the page title in the specified browser.


That's it! You should now be able to deploy Selenium nodes in Kubernetes, run the test scripts for different browsers, and manage the Python dependencies using the provided Makefile. The goal is to grow this into some better tests to be run in the CI phase for arbitrary web applications.
