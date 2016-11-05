# Make sure the Apt package lists are up to date, so we're downloading versions that exist.
cookbook_file "apt-sources.list" do
	path "/etc/apt/sources.list"
end
execute "apt_update" do
	command "apt-get update"
end

# Base configuration recipe in Chef.
package "wget"
package "ntp"
cookbook_file "ntp.conf" do
	path "/etc/ntp.conf"
end
execute "ntp_restart" do
	command "service ntp restart"
end

  execute "Installing dos2unix for Windows machines" do
      command "apt-get install dos2unix -y"
  end
  
  
  # Install Django Web-Frameworks and packages
  package "git"
  package "python-pip"
  package "libpq-dev python-dev"
  package "postgresql"
  package "nginx"
  package "libjpeg-dev"
  
  execute "Installing Django and libraries" do
      command "sudo pip install django==1.8 requests django_countries geoip2 django-ipware uwsgi Pillow psycopg2 spotipy django-bootstrap3-datetimepicker django-datetime-widget django-allauth"
      user 'vagrant'
  end
  
  execute "Installing Crispy for bootstrapping forms with ease" do
      command "sudo pip install --upgrade django-crispy-forms"
      user 'vagrant'
  end


execute "Installing Crispy for bootstrapping forms with ease" do
	command "sudo pip install --upgrade django-crispy-forms"
	user 'vagrant'
end

  execute "Creating makemigrations on apps for project" do
      cwd "/home/vagrant/projectCityEvents"
      command 'python manage.py makemigrations eventSearch EventDetails accounts userCreateEvents saveEvents'
  end

execute 'create database' do
	cwd '/home/vagrant/projectCityEvents/'
	command 'python manage.py migrate'
end

execute 'load fake data' do
	cwd '/home/vagrant/projectCityEvents/'
	command 'python manage.py loaddata userEventsData.json'	
end

 execute 'Collecting static files' do
     cwd '/home/vagrant/projectCityEvents/'
     command 'python manage.py collectstatic --noinput'
 end
 
 # Configuring WSGI 
 cookbook_file "rc.local" do
     path "/etc/rc.local"
 end
 
 execute "Converting rc.local to be OS agnostic" do
     command 'sudo dos2unix /etc/rc.local /home/vagrant/projectCityEvents/restart.sh'
 end
 
 execute "Starting WSGI process" do
     command '/etc/rc.local'
 end
 
 # Configuring Webserver
 cookbook_file "nginx-default" do
     path "/etc/nginx/sites-available/default"
 end
 
 service "nginx" do
     action :restart
 end

