Name:           ros-hydro-moveit-ros-benchmarks
Version:        0.5.20
Release:        0%{?dist}
Summary:        ROS moveit_ros_benchmarks package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-eigen-conversions
Requires:       ros-hydro-moveit-ros-planning
Requires:       ros-hydro-moveit-ros-warehouse
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-eigen-conversions
BuildRequires:  ros-hydro-moveit-ros-planning
BuildRequires:  ros-hydro-moveit-ros-warehouse
BuildRequires:  ros-hydro-rosconsole
BuildRequires:  ros-hydro-roscpp

%description
MoveIt tools for benchmarking

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Dec 09 2014 Ioan Sucan <isucan@google.com> - 0.5.20-0
- Autogenerated by Bloom

