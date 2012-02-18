%bcond_without bootstrap
%global packname  spatstat
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.25_3
Release:          1
Summary:          Spatial Point Pattern analysis, model-fitting, simulation, tests
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.25-3.tar.gz
Requires:         R-stats R-graphics R-utils R-mgcv R-deldir 
%if %{with bootstrap}
Requires:         R-gpclib R-sm R-spatial R-rpanel R-tkrplot R-scatterplot3d R-RandomFields 
%else
Requires:         R-gpclib R-sm R-maptools R-spatial R-rpanel R-tkrplot R-scatterplot3d R-RandomFields 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-graphics R-utils R-mgcv R-deldir
%if %{with bootstrap}
BuildRequires:    R-gpclib R-sm R-spatial R-rpanel R-tkrplot R-scatterplot3d R-RandomFields 
%else
BuildRequires:    R-gpclib R-sm R-maptools R-spatial R-rpanel R-tkrplot R-scatterplot3d R-RandomFields 
%endif

%description
A package for analysing spatial data, mainly Spatial Point Patterns,
including multitype/marked points and spatial covariates, in any
two-dimensional spatial region. Also supports three-dimensional point
patterns, and space-time point patterns in any number of dimensions. 
Contains over 1000 functions for plotting spatial data, exploratory data
analysis, model-fitting, simulation, spatial sampling, model diagnostics,
and formal inference.  Data types include point patterns, line segment
patterns, spatial windows, pixel images and tessellations.  Exploratory
methods include K-functions, nearest neighbour distance and empty space
statistics, Fry plots, pair correlation function, kernel smoothed
intensity, relative risk estimation with cross-validated bandwidth
selection, mark correlation functions, segregation indices, mark
dependence diagnostics etc.  Point process models can be fitted to point
pattern data using functions ppm, kppm, slrm similar to glm. Models may
include dependence on covariates, interpoint interaction, cluster
formation and dependence on marks. Fitted models can be simulated
automatically.  Also provides facilities for formal inference (such as
chi-squared tests) and model diagnostics (including simulation envelopes,
residuals, residual plots and Q-Q plots).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/ratfor
