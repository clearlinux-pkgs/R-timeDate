#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-timeDate
Version  : 3012.100
Release  : 17
URL      : http://cran.r-project.org/src/contrib/timeDate_3012.100.tar.gz
Source0  : http://cran.r-project.org/src/contrib/timeDate_3012.100.tar.gz
Summary  : Rmetrics - Chronological and Calendar Objects
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n timeDate

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library timeDate
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library timeDate


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/timeDate/COPYRIGHT.html
/usr/lib64/R/library/timeDate/DESCRIPTION
/usr/lib64/R/library/timeDate/INDEX
/usr/lib64/R/library/timeDate/Meta/Rd.rds
/usr/lib64/R/library/timeDate/Meta/hsearch.rds
/usr/lib64/R/library/timeDate/Meta/links.rds
/usr/lib64/R/library/timeDate/Meta/nsInfo.rds
/usr/lib64/R/library/timeDate/Meta/package.rds
/usr/lib64/R/library/timeDate/NAMESPACE
/usr/lib64/R/library/timeDate/R/timeDate
/usr/lib64/R/library/timeDate/R/timeDate.rdb
/usr/lib64/R/library/timeDate/R/timeDate.rdx
/usr/lib64/R/library/timeDate/help/AnIndex
/usr/lib64/R/library/timeDate/help/aliases.rds
/usr/lib64/R/library/timeDate/help/paths.rds
/usr/lib64/R/library/timeDate/help/timeDate.rdb
/usr/lib64/R/library/timeDate/help/timeDate.rdx
/usr/lib64/R/library/timeDate/html/00Index.html
/usr/lib64/R/library/timeDate/html/R.css
/usr/lib64/R/library/timeDate/unitTests/Makefile
/usr/lib64/R/library/timeDate/unitTests/runTests.R
/usr/lib64/R/library/timeDate/unitTests/runit.AAA.R
/usr/lib64/R/library/timeDate/unitTests/runit.Class.R
/usr/lib64/R/library/timeDate/unitTests/runit.Coercion.R
/usr/lib64/R/library/timeDate/unitTests/runit.DaylightSavingTime.R
/usr/lib64/R/library/timeDate/unitTests/runit.FinCenter.R
/usr/lib64/R/library/timeDate/unitTests/runit.HolidayCalendars.R
/usr/lib64/R/library/timeDate/unitTests/runit.HolidayDates.R
/usr/lib64/R/library/timeDate/unitTests/runit.MathOps.R
/usr/lib64/R/library/timeDate/unitTests/runit.SpecialDates.R
/usr/lib64/R/library/timeDate/unitTests/runit.Subsets.R
/usr/lib64/R/library/timeDate/unitTests/runit.ZZZ.R
/usr/lib64/R/library/timeDate/unitTests/runit.dayOfWeek.R
/usr/lib64/R/library/timeDate/unitTests/runit.dayOfYear.R
/usr/lib64/R/library/timeDate/unitTests/runit.isWeekday.R
/usr/lib64/R/library/timeDate/unitTests/runit.isWeekend.R
/usr/lib64/R/library/timeDate/unitTests/runit.seq.R
