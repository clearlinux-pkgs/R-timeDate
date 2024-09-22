#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v20
# autospec commit: f35655a
#
Name     : R-timeDate
Version  : 4041.110
Release  : 87
URL      : https://cran.r-project.org/src/contrib/timeDate_4041.110.tar.gz
Source0  : https://cran.r-project.org/src/contrib/timeDate_4041.110.tar.gz
Summary  : Rmetrics - Chronological and Calendar Objects
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
standard as well as of the ANSI C and POSIX standards. Beyond
	these standards it provides the "Financial Center" concept
	which allows to handle data records collected in different time 
	zones and mix them up to have always the proper time stamps with 
	respect to your personal financial center, or alternatively to the GMT
	reference time. It can thus also handle time stamps from historical 
	data records from the same time zone, even if the financial 
	centers changed day light saving times at different calendar
	dates.

%prep
%setup -q -n timeDate
pushd ..
cp -a timeDate buildavx2
popd
pushd ..
cp -a timeDate buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727023573

%install
export SOURCE_DATE_EPOCH=1727023573
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/timeDate/COPYRIGHT.html
/usr/lib64/R/library/timeDate/DESCRIPTION
/usr/lib64/R/library/timeDate/INDEX
/usr/lib64/R/library/timeDate/Meta/Rd.rds
/usr/lib64/R/library/timeDate/Meta/features.rds
/usr/lib64/R/library/timeDate/Meta/hsearch.rds
/usr/lib64/R/library/timeDate/Meta/links.rds
/usr/lib64/R/library/timeDate/Meta/nsInfo.rds
/usr/lib64/R/library/timeDate/Meta/package.rds
/usr/lib64/R/library/timeDate/NAMESPACE
/usr/lib64/R/library/timeDate/NEWS.md
/usr/lib64/R/library/timeDate/R/sysdata.rdb
/usr/lib64/R/library/timeDate/R/sysdata.rdx
/usr/lib64/R/library/timeDate/R/timeDate
/usr/lib64/R/library/timeDate/R/timeDate.rdb
/usr/lib64/R/library/timeDate/R/timeDate.rdx
/usr/lib64/R/library/timeDate/_pkgdown.yml
/usr/lib64/R/library/timeDate/help/AnIndex
/usr/lib64/R/library/timeDate/help/aliases.rds
/usr/lib64/R/library/timeDate/help/paths.rds
/usr/lib64/R/library/timeDate/help/timeDate.rdb
/usr/lib64/R/library/timeDate/help/timeDate.rdx
/usr/lib64/R/library/timeDate/html/00Index.html
/usr/lib64/R/library/timeDate/html/R.css
/usr/lib64/R/library/timeDate/pkgdown.yml
/usr/lib64/R/library/timeDate/tests/doRUnit.R
/usr/lib64/R/library/timeDate/unitTests/Makefile
/usr/lib64/R/library/timeDate/unitTests/holidayLONDON_1834_to_2024_corrected.rds
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
