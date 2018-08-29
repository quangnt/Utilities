# Setup Jmeter:
	- Download Jmeter 4.0 from [Download](https://jmeter.apache.org/download_jmeter.cgi) and extract it to folder
	- Set JMETER_HOME = <path to extract folder>, then add `%JMETER_HOME%\bin;` to PATH environment variable	
	- Download plugin [Property File Reader](http://www.testautomationguru.com/download/87/) and put it into `%JMETER_HOME\lib\ext`
	- Add follow line in `%JMETER_HOME%\bin\jmeter.properties` to delete old result and write new file:
		`resultcollector.action_if_file_exists=DELETE` (without "`")
	- Add follow properties line to enable generate html report
		`jmeter.save.saveservice.bytes=true
		# Only available with HttpClient4
		#jmeter.save.saveservice.sent_bytes=true
		jmeter.save.saveservice.label=true
		jmeter.save.saveservice.latency=true
		jmeter.save.saveservice.response_code=true
		jmeter.save.saveservice.response_message=true
		jmeter.save.saveservice.successful=true
		jmeter.save.saveservice.thread_counts=true
		jmeter.save.saveservice.thread_name=true
		jmeter.save.saveservice.time=true
		jmeter.save.saveservice.connect_time=true
		jmeter.save.saveservice.assertion_results_failure_message=true
		# the timestamp format must include the time and should include the date.
		# For example the default, which is milliseconds since the epoch: 
		jmeter.save.saveservice.timestamp_format=ms`
# To Run Jmeter performance test script:
	- Run Jmeter test plan via command prompt:
		`jmeter -n -t C:\Users\t-nquang\PerformanceTest\TBV_PerformanceTest.jmx -l C:\Users\t-nquang\PerformanceTest\TBV_PerformanceTest09012018.jtl`
	- Generate Report html bases on test plan:			
		`jmeter -g C:\Users\t-nquang\PerformanceTest\TBV_PerformanceTest290108.jtl -o C:\Users\t-nquang\PerformanceTest\Result`
		+ Note: To enable output html report need to enable following properties in `%JMETER_HOME\bin\jmeter.properties`
			

# Troubleshooting problem:
	- Encounter `WARNING: Could not open/create prefs root node Software\JavaSoft\Prefs at root 0x80000002. Windows RegCreateKeyEx(...) returned error code 5` when run jmeter from command line, 
	refer to [solution](https://stackoverflow.com/questions/16428098/groovy-shell-warning-could-not-open-create-prefs-root-node)
	
