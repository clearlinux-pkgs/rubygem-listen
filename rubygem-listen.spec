#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-listen
Version  : 3.0.8
Release  : 6
URL      : https://rubygems.org/downloads/listen-3.0.8.gem
Source0  : https://rubygems.org/downloads/listen-3.0.8.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-listen-bin
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-rb-fsevent
BuildRequires : rubygem-rb-inotify
BuildRequires : rubygem-rdoc

%description
:exclamation: Listen is currently accepting more maintainers. Please [read this](https://github.com/guard/guard/wiki/Maintainers) if you're interested in joining the team.

%package bin
Summary: bin components for the rubygem-listen package.
Group: Binaries

%description bin
bin components for the rubygem-listen package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n listen-3.0.8
gem spec %{SOURCE0} -l --ruby > rubygem-listen.gemspec

%build
gem build rubygem-listen.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
listen-3.0.8.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/listen-3.0.8.gem
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/CHANGELOG.md
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/CONTRIBUTING.md
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/README.md
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/bin/listen
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/adapter.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/adapter/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/adapter/bsd.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/adapter/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/adapter/darwin.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/adapter/linux.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/adapter/polling.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/adapter/windows.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/backend.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/change.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/directory.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/event/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/event/loop.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/event/processor.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/event/queue.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/file.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/fsm.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/internals/thread_pool.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/listener.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/listener/config.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/logger.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/queue_optimizer.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/record.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/record/entry.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/record/symlink_detector.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/silencer.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/silencer/controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/listen-3.0.8/lib/listen/version.rb
/usr/lib64/ruby/gems/2.3.0/specifications/listen-3.0.8.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/listen
