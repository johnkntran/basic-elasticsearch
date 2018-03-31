# basic-elasticsearch
A basic demonstration of using ElasticSearch to render search results.

## Installation

### Install Oracle Java 8 JDK
1. Check if you have an existing installation of Java by executing `java -version`.
2. If not, download the latest official Java version from Oracle by executing `wget --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-i586.tar.gz`.
3. Add Oracle's PPA `sudo add-apt-repository ppa:webupd8team/java` and then update the package manager `sudo apt-get update`.
4. Install Oracle JDK 8 by executing `sudo apt-get install oracle-java8-installer`. You will need to accept the license agreement in the Terminal.
5. Ensure that the installed Oracle JDK 8 is the default installation (if there are multiple Java versions on the system) with `sudo update-alternatives --config java`.
6. Many programs use the JAVA_HOME environment variable to figure out where Java is installed. Open the /etc/environment file (in Vim or otherwise) and add a line at the end that says `JAVA_HOME="/usr/lib/jvm/java-8-oracle"`.
7. Refresh the terminal by executing `source /etc/environment`. Then ensure the JAVA_HOME variable is loaded by typing `echo $JAVA_HOME`. Check the Java is properly installed by typing `java -version`.

- Source: https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-get-on-ubuntu-16-04

