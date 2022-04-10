def tools = load "/groovy/tools.groovy"

pipeline {
    agent any
	options {
		timestamps()	//显示日志时间
		skipDefaultCheckout()	//删除隐式checkout scm语句
		disableConcurrentBuilds() //禁止并行
		timeout(time: 1, unit : 'HOURS')	//流水线超时设置1h
	}
    stages {
		//下载代码
        stage('GetCode') {
            steps {
				timeout(time:5, unit:"MINUTES"){
					script { 
					 echo("Stage GetCode")
					 tools.PrintMsg("test Tool Func")
					}
				}
            }
        }
		//构建
		stage('BuildCode') {
            steps {
				timeout(time:5, unit:"MINUTES"){
					script { 
					 echo("Stage BuildCode")
					}
				}
            }
        }
		//扫描代码
		stage('ScanCode') {
            steps {
				timeout(time:5, unit:"MINUTES"){
					script { 
					 echo("Stage ScanCode")
					}
				}
            }
        }
    }
	post{
		always{
			script{
				echo("always")
			}
		}
		success{
			script{
				echo("success")
				currentBuild.description = "Build Success"
			}
		}
		failure{
			script{
				echo("failure")
				currentBuild.description = "Build Failure"
			}
		}
		aborted{
			script{
				echo("aborted")
				currentBuild.description = "Build Aborted"
			}
		}
	}
}