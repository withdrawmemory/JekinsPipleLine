pipeline {
    agent any
	
	parameters {
        booleanParam(defaultValue:true, description: '',name: 'userFlag')
		choice(name: 'choiceParam', choices: ['one', 'two', 'three'], description: '')
    }
	
	options {
		timestamps()	//显示日志时间
		//skipDefaultCheckout()	//删除隐式checkout scm语句
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
					 echo(params.testStr)
					 def tools = load"${env.WORKSPACE}/groovy/tools.groovy"
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
					 echo("Stage GetCode")
					 echo "One args:$userFlag\n Two args:$choiceParam"
					 def logFile = "test.Log"
					 sh """
					    echo "Log Path is ${logFile}"
						python -u -c "import LogHelper; LogHelper.SaveLog('${logFile}')"
					 """
					 echo("%userFlag")
					 echo("End Stage GetCode")
					}
				}
            }
        }
		//扫描代码
		stage('ScanCode') {
            steps {
				 archiveArtifacts artifacts: '**/*.groovy', fingerprint: true 
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