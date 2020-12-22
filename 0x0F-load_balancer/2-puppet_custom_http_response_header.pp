# creating a custom HTTP header response, but with Puppet.

exec { 'Update':
  command => 'sudo apt-get update',
  path    => ['/usr/bin', '/bin'],
}

package { 'Install nginx':
  ensure  => installed,
  require => Exec['update'],
  name    => 'nginx'
}

file_line { 'append line in nginx config file':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server',
  line   => "\tadd_header X-Served-By ${hostname};",
}

exec { 'restart nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
}
