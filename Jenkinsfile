pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Notify and Approve') {
            steps {
                script {
                    def prUrl = env.CHANGE_URL
                    echo "A new pull request requires your approval: ${prUrl}"

                    // Wait for manager approval
                    input message: 'Approve this pull request?', ok: 'Approve'
                }
            }
        }

        stage('Merge PR') {
            steps {
                script {
                    def prNumber = env.CHANGE_ID
                    def repoOwner = env.GIT_URL.split('/')[3]
                    def repoName = env.GIT_URL.split('/')[4].replace('.git', '')

                    // Merge the pull request using GitHub API
                    def mergeUrl = "https://api.github.com/repos/${repoOwner}/${repoName}/pulls/${prNumber}/merge"
                    def mergeData = [commit_title: 'Merged by Jenkins pipeline', merge_method: 'merge']
                    def response = httpRequest(
                        acceptType: 'APPLICATION_JSON',
                        contentType: 'APPLICATION_JSON',
                        httpMode: 'PUT',
                        requestBody: new groovy.json.JsonBuilder(mergeData).toString(),
                        url: mergeUrl,
                        customHeaders: [[name: 'Authorization', value: "token ${GITHUB_TOKEN}"]]
                    )
                    echo "PR Merged: ${response}"
                }
            }
        }
    }
}
