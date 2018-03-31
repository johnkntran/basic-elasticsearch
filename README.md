# basic-elasticsearch
A basic demonstration of using Elasticsearch to render search results.

## Installation

### Install Oracle Java 8 JDK
1. Check if you have an existing installation of Java by executing `java -version`.
2. If not, download the latest official Java version from Oracle by executing `wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-i586.tar.gz`.
3. Add Oracle's PPA `sudo add-apt-repository ppa:webupd8team/java` and then update the package manager `sudo apt-get update`.
4. Install Oracle JDK 8 by executing `sudo apt-get install oracle-java8-installer`. You will need to accept the license agreement in the Terminal.
5. Ensure that the installed Oracle JDK 8 is the default installation (if there are multiple Java versions on the system) with `sudo update-alternatives --config java`.
6. Many programs use the JAVA_HOME environment variable to figure out where Java is installed. Open the */etc/environment* file (in Vim or otherwise) and add a line at the end that says `JAVA_HOME="/usr/lib/jvm/java-8-oracle"`.
7. Refresh the terminal by executing `source /etc/environment`. Then ensure the JAVA_HOME variable is loaded by typing `echo $JAVA_HOME`. Check the Java is properly installed by typing `java -version`.
- Source: https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04

### Install Elasticsearch 6.x
1. Obtain an Elasticsearch Signing Key by executing `wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -`.
2. Install the apt-transport-https library with `sudo apt-get install apt-transport-https`.
3. Save the repository definition with `echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list`.
4. Install the Elasticsearch Debian package with `sudo apt-get update && sudo apt-get install elasticsearch`.
5. Your Elasticsearch cluster should be up and running. View its status by typing `sudo systemctl status elasticsearch`. And test an HTTP request by issuing `curl -X GET 'localhost:9200'` and `curl -X GET 'localhost:9200/_cat/health?v'`.

- Source: https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html#install-deb
- Source: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-16-04

### Create an Index and Batch Load Data
1. Create an index called *quotes* with `curl -XPUT 'localhost:9200/quotes?pretty&pretty'`, then `curl -XGET 'localhost:9200/_cat/indices?v&pretty'` (the yellow status is ok).
2. Bulk import all the quotes data by first moving into the data directory `cd ./basic-elasticsearch/data`, then issueing `curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/_bulk --data-binary "@bulk.json"`.
3. Test by issueing `curl -XGET 'localhost:9200/quotes/_search' -H "Content-Type: application/json" -d '{"query": {"match_all": {}}}'` (which returns a summary of all 1,842 results, plus the first 10 records) and `curl -XGET 'localhost:9200/quotes/_search?q=quote:moon'` (which should return 4 results).
4. If for some reason you need to delete the index and start over, executing `curl -XDELETE 'localhost:9200/quotes?pretty&pretty'` will delete the index.

- Source: https://www.elastic.co/guide/en/elasticsearch/reference/current/_create_an_index.html
- Source: https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html
- Source: http://queirozf.com/entries/elasticsearch-bulk-inserting-examples

### Configure Elasticseach to Allow Traffic
1. In progress...
