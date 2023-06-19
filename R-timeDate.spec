#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-timeDate
Version  : 4022.108
Release  : 83
URL      : https://cran.r-project.org/src/contrib/timeDate_4022.108.tar.gz
Source0  : https://cran.r-project.org/src/contrib/timeDate_4022.108.tar.gz
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
cd %{_builddir}/timeDate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678828178

%install
export SOURCE_DATE_EPOCH=1678828178
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
