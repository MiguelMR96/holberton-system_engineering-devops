# creating a custom HTTP header response, but with Puppet.

exec { 'apt-get update':
command => 'sudo apt-get update',
path    => ['/usr/bin', '/bin'],
}

package { 'install nginx':
ensure => installed,
name   => 'nginx',
}

file_line { 'append line in nginx config file':
ensure => present,
path   => '/etc/nginx/sites-available/default',
after  => 'server_name _;',
line   => "add_header X-Served-By ${hostname};",
}

exec { 'restart nginx':
command => 'sudo service nginx restart',
path    => ['/usr/bin', '/bin'],
}
