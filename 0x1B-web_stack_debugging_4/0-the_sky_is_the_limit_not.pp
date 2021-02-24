# Puppet that change the limit of open files in an Nginx server.
exec { 'sed':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => "sed -i 's/15/1024/' /etc/default/nginx",
}
-> exec { 'restart':
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  command => 'service nginx restart',
}
