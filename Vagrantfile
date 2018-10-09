# Copyright (c) 2018-present eyeo GmbH
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# https://docs.ruby-lang.org/en/trunk/RDoc/Require.html
require 'vagrant'

# https://www.vagrantup.com/docs/vagrantfile/vagrant_version.html
Vagrant.require_version '>= 1.9.0'

# https://www.vagrantup.com/docs/vagrantfile/version.html
Vagrant.configure(2) do |vagrant|

  # https://www.vagrantup.com/docs/vagrantfile/machine_settings.html
  vagrant.vm.box = 'debian/stretch64'
  vagrant.vm.box_check_update = false
  vagrant.vm.post_up_message = nil

  # https://www.vagrantup.com/docs/multi-machine/
  vagrant.vm.define('example') do |config|

    # https://www.vagrantup.com/docs/vagrantfile/machine_settings.html
    config.vm.hostname = 'example.com'

    # https://www.vagrantup.com/docs/networking/forwarded_ports.html
    config.vm.network "forwarded_port", guest: 8080, host: 8080

    # https://www.vagrantup.com/docs/provisioning/ansible.html
    config.vm.provision('ansible') do |ansible|
      ansible.verbose = 'v'
      ansible.playbook = 'playbook.yml'
    end

  end

end
