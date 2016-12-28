Name: ffmpeg
Version: 3.2.2
Release: alt5
%define enable_license_lgplv3 0

# old libx265 from sisyphus doesn't fit, newer is needed. Add new libx265 version to sisyphus and use it (but does it break existing programs??). Or set next flag to 0 (the safe way)
%define use_libx265 1

%define libs_suffix -ffmpeg-renamed-libs
%define libsff avcodec%libs_suffix avdevice%libs_suffix avfilter%libs_suffix avformat%libs_suffix avresample%libs_suffix avutil%libs_suffix postproc%libs_suffix swresample%libs_suffix swscale%libs_suffix
%define libs avcodec avdevice avfilter avformat avresample avutil postproc swresample swscale

%define repo_p7 0

Summary: FFmpeg libraries (renamed) and programs


License: GPLv3+
Group: Video
Url: https://github.com/FFmpeg/FFmpeg

Packager: Sample Maintainer <samplemaintainer@altlinux.org>
BuildPreReq: yasm
%if %repo_p7
BuildPreReq: gcc-c++
%else
BuildPreReq: gcc5-c++
%endif
BuildPreReq: libchromaprint-devel frei0r-devel libgcrypt-devel libgmp-devel libgnutls-devel ladspa_sdk libass-devel libbluray-devel libbs2b-devel libcaca-devel libcelt-devel libcdio-devel libdc1394-devel flite-devel fontconfig-devel libfreetype-devel libfribidi-devel libgme-devel libgsm-devel libiec61883-devel libilbc-devel libmodplug-devel liblame-devel libnut-devel libopencore-amrnb-devel libopencore-amrwb-devel libopencv-devel libopenjpeg-devel
%if %repo_p7
%else
BuildPreReq: libopenjpeg2.0-devel
%endif
BuildPreReq: libopus-devel
BuildPreReq: libpulseaudio-devel
BuildPreReq: librubberband-devel
BuildPreReq: librtmp-devel
BuildPreReq: libschroedinger-devel
BuildPreReq: libsmbclient-devel
BuildPreReq: libsnappy-devel
BuildPreReq: libsoxr-devel
BuildPreReq: libspeex-devel
BuildPreReq: libssh2-devel
BuildPreReq: libssh-devel
BuildPreReq: tesseract-devel
BuildPreReq: libtheora-devel
BuildPreReq: libtwolame-devel
BuildPreReq: libv4l-devel
BuildPreReq: libvo-amrwbenc-devel
BuildPreReq: libvorbis-devel
BuildPreReq: libvpx-devel
BuildPreReq: libwavpack-devel
BuildPreReq: libwebp-devel
BuildPreReq: libwebp-tools
BuildPreReq: libx264-devel

%if %repo_p7
%else
BuildPreReq: libx265-devel
%endif
BuildPreReq: libxcb-devel
BuildPreReq: libxcbutil-keysyms-devel
BuildPreReq: libxcb-render-util
BuildPreReq: libxcb-render-util-devel
BuildPreReq: libxcbutil-devel
BuildPreReq: libxcbutil-icccm-devel
BuildPreReq: libxcbutil-image-devel
%if %repo_p7
%else
BuildPreReq: libxcbutil-xrm-devel
BuildPreReq: libxcbutil-cursor-devel
BuildPreReq: libxcbutil-proto
%endif
BuildPreReq: libxvid-devel
BuildPreReq: libzeromq-devel
BuildPreReq: libzvbi-devel
BuildPreReq: libnetcdf-devel
BuildPreReq: libopenal-devel
BuildPreReq: fglrx_glx
BuildPreReq: libGL-devel
BuildPreReq: libGLU-devel
BuildPreReq: libfreeglut-devel
%if %repo_p7
%else
BuildPreReq: libcdio-paranoia-devel
%endif
Source: %name-%version.tar

%description
FFmpeg libraries, with suffix "-ffmpeg-renamed-libs" added to all libs
and their folders in /usr/include, to avoid conflict with libav. And
FFmpeg programs: ffprobe, ffmpeg, ffserver




%package doc
Summary: Documentation files for FFmpeg
Group: Video
BuildArch: noarch

%description doc
Documentation files for FFmpeg



%package programs
Summary: ffmpeg, ffprobe, ffserver. From FFmpeg package
Group: Video

%description programs
ffmpeg, ffprobe, ffserver. From FFmpeg package





%prep
%setup





%build
# non-autotools configure
%ifarch x86_64
  var_arch="x86_64"
%else
  var_arch="i586"
%endif
# --enable-avresample
# frei0r is gpl, use --enable-gpl
# librubberband is gpl
# libsmbclient is gpl
# libx264 is gpl
# libxvid is gpl
# .c files for libbut cause compulation errors (smth like trying to access member of smth which is not union or struct)
# gmp is LGPLv3, use --enable-version3
# libiec61883 not found
# libcelt must be installed and version >= 0.11.0
# libflite not found
# libilbc not found
# libx265 versin must be 68
# opencl not found
# no usable libcdio/cdparanoia found (install libcdio-paranoia-devel?)

#conf_lib_opts="--enable-chromaprint --enable-frei0r --enable-gcrypt --enable-gmp --enable-gnutls --enable-ladspa --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libcelt --enable-libcdio --enable-libdc1394 --enable-libflite --enable-libfontconfig --enable-libfreetype --enable-libfribidi --enable-libgme --enable-libgsm --enable-libiec61883 --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libnut --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopencv --enable-libopenjpeg --enable-libopus --enable-libpulse --enable-librubberband --enable-librtmp --enable-libschroedinger --enable-libsmbclient --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libssh --enable-libtesseract --enable-libtheora --enable-libtwolame --enable-libv4l2 --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxvid --enable-libzmq --enable-libzvbi --enable-netcdf --enable-openal --enable-opencl --enable-opengl"

#--enable-libvpx 
#conf_lib_opts=""
conf_lib_opts="--enable-chromaprint
%if %use_libx265
  --enable-libx265
%endif
  --enable-gcrypt
  --enable-gmp
  --enable-gnutls
  --enable-ladspa
%if %repo_p7
%else
  --enable-libass
%endif
  --enable-libbluray
  --enable-libbs2b
  --enable-libcaca
%if %repo_p7
%else
  --enable-libcdio
%endif
  --enable-libdc1394
  --enable-libfontconfig
  --enable-libfreetype
  --enable-libfribidi
  --enable-libgme
  --enable-libgsm
  --enable-libmodplug
  --enable-libmp3lame
  --enable-libopencore-amrnb
  --enable-libopencore-amrwb
  --enable-libopencv
  --enable-libopenjpeg
  --enable-libopus
  --enable-libpulse
  --enable-librtmp
  --enable-libschroedinger
  --enable-libsnappy
  --enable-libsoxr
  --enable-libspeex
  --enable-libssh
%if %repo_p7
%else
  --enable-libtesseract
%endif
  --enable-libtheora
  --enable-libtwolame
  --enable-libv4l2
  --enable-libvo-amrwbenc
  --enable-libvorbis
  --enable-libwavpack
  --enable-libwebp
  --enable-libzmq
  --enable-libzvbi
  --enable-netcdf
  --enable-openal
  --enable-opengl
  --enable-version3
%if %enable_license_lgplv3
  --enable-gmp
%endif
  --enable-gpl
  --enable-frei0r
%if %repo_p7
%else
  --enable-librubberband
%endif
  --enable-libsmbclient
  --enable-libx264
  --enable-libxvid
  --enable-libvpx"
%ifarch x86_64
  yasm_opt="--enable-yasm"
#  strip_opt=""
  extra_opts=""
%else
  yasm_opt="--disable-yasm"
#  strip_opt="--disable-stripping"
#  extra_opts="--disable-asm"
  extra_opts=""
%endif
./configure --prefix=/usr --enable-avcodec --enable-avformat --enable-avfilter --enable-avdevice --enable-swscale --enable-swresample --arch=$var_arch --cpu=$var_arch $yasm_opt --enable-shared --enable-static --libdir=%_libdir --enable-pic --enable-avresample --build-suffix=%libs_suffix $extra_opts $conf_lib_opts
make clean
#%%make_build LDFLAGS=-Wl,--warn-unresolved-symbols
%make_build




%install

%makeinstall_std


# include dirs don't get renamed like .so and .a files. Rename manually
pushd %buildroot/usr/include
for lib in %libs ; do
  mv lib${lib} lib${lib}%{libs_suffix}
done

var_fflibs="%libs"

var_sed_e=""

for lib in $var_fflibs ; do
  var_sed_e="${var_sed_e} -e \"s/lib(${lib})/lib\\1%{libs_suffix}/g\""
done


find -type f -name "*.c" -exec bash -c "sed -E -i.bak ${var_sed_e} {} ; rm {}.bak -f" \;
find -type f -name "*.h" -exec bash -c "sed -E -i.bak ${var_sed_e} {} ; rm {}.bak -f" \;
find -type f -name "*.cpp" -exec bash -c "sed -E -i.bak ${var_sed_e} {} ; rm {}.bak -f" \;
find -type f -name "*.hpp" -exec bash -c "sed -E -i.bak ${var_sed_e} {} ; rm {}.bak -f" \;
popd


# rename libs inside .pc files (pkgconfig)
pushd %buildroot%_libdir/pkgconfig
var_fflibs="%libs"

# seems it's done already, configure --build-suffix worked?
#for lib in $var_fflibs ; do
#  mv lib${lib}.pc lib${lib}%%{libs_suffix}.pc
#done

var_sed_e=""

for lib in $var_fflibs ; do
  var_sed_e="${var_sed_e} -e \"s/^\\s*Name:\\s+lib(${lib})/Name: lib\\1%{libs_suffix}/g\""
done


find -type f -name "*.pc" -exec bash -c "sed -E -i.bak ${var_sed_e} {} ; rm {}.bak -f" \;
popd

RPM_VERIFY_ELF_METHOD="relaxed"

%files doc
%doc Changelog CONTRIBUTING.md CREDITS INSTALL.md LICENSE.md MAINTAINERS README.md RELEASE RELEASE_NOTES

%files programs
%_bindir/*
/usr/share/ffmpeg



%changelog
* Wed Dec 28 2016 Konstantin Yablochkin <konstyab@altlinux.org> 3.2.2-alt5
- switch to GPLv2
* Sun Dec 11 2016 Sample Maintainer <samplemaintainer@altlinux.org> 3.2.2-alt4
- change libs suffix to -ffmpeg-renamed-libs
- add ffmpeg-renamed-libs, ffmpeg-renamed-libs-devel packages
* Sun Dec 11 2016 Sample Maintainer <samplemaintainer@altlinux.org> 3.2.2-alt3
- fixed i586 ./configure flags
* Fri Dec 09 2016 Sample Maintainer <samplemaintainer@altlinux.org> 3.2.2-alt2
- initial build








####### AUTOMATICALLY GENERATED PART ######


%package -n libavcodec%{libs_suffix}
Summary: avcodec library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libavcodec%{libs_suffix}-devel
Summary: Headers, .pc and .so for libavcodec%{libs_suffix}
Group: Development/C
Requires: libavcodec%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavcodec%{libs_suffix}-devel-static
Summary: .a for libavcodec%{libs_suffix}
Group: Development/C
Requires: libavcodec%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavformat%{libs_suffix}
Summary: avformat library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libavformat%{libs_suffix}-devel
Summary: Headers, .pc and .so for libavformat%{libs_suffix}
Group: Development/C
Requires: libavformat%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavformat%{libs_suffix}-devel-static
Summary: .a for libavformat%{libs_suffix}
Group: Development/C
Requires: libavformat%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavutil%{libs_suffix}
Summary: avutil library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libavutil%{libs_suffix}-devel
Summary: Headers, .pc and .so for libavutil%{libs_suffix}
Group: Development/C
Requires: libavutil%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavutil%{libs_suffix}-devel-static
Summary: .a for libavutil%{libs_suffix}
Group: Development/C
Requires: libavutil%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavfilter%{libs_suffix}
Summary: avfilter library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libavfilter%{libs_suffix}-devel
Summary: Headers, .pc and .so for libavfilter%{libs_suffix}
Group: Development/C
Requires: libavfilter%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavfilter%{libs_suffix}-devel-static
Summary: .a for libavfilter%{libs_suffix}
Group: Development/C
Requires: libavfilter%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavdevice%{libs_suffix}
Summary: avdevice library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libavdevice%{libs_suffix}-devel
Summary: Headers, .pc and .so for libavdevice%{libs_suffix}
Group: Development/C
Requires: libavdevice%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavdevice%{libs_suffix}-devel-static
Summary: .a for libavdevice%{libs_suffix}
Group: Development/C
Requires: libavdevice%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d

%package -n libswresample%{libs_suffix}
Summary: swresample library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libswresample%{libs_suffix}-devel
Summary: Headers, .pc and .so for libswresample%{libs_suffix}
Group: Development/C
Requires: libswresample%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libswresample%{libs_suffix}-devel-static
Summary: .a for libswresample%{libs_suffix}
Group: Development/C
Requires: libswresample%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d

%package -n libswscale%{libs_suffix}
Summary: swscale library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libswscale%{libs_suffix}-devel
Summary: Headers, .pc and .so for libswscale%{libs_suffix}
Group: Development/C
Requires: libswscale%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libswscale%{libs_suffix}-devel-static
Summary: .a for libswscale%{libs_suffix}
Group: Development/C
Requires: libswscale%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavresample%{libs_suffix}
Summary: avresample library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libavresample%{libs_suffix}-devel
Summary: Headers, .pc and .so for libavresample%{libs_suffix}
Group: Development/C
Requires: libavresample%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libavresample%{libs_suffix}-devel-static
Summary: .a for libavresample%{libs_suffix}
Group: Development/C
Requires: libavresample%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d

%package -n libpostproc%{libs_suffix}
Summary: postproc library from FFmpeg
Group: System/Libraries
%filter_from_requires /^\/.*/d

%package -n libpostproc%{libs_suffix}-devel
Summary: Headers, .pc and .so for libpostproc%{libs_suffix}
Group: Development/C
Requires: libpostproc%{libs_suffix} = %version-%release
%filter_from_requires /^\/.*/d

%package -n libpostproc%{libs_suffix}-devel-static
Summary: .a for libpostproc%{libs_suffix}
Group: Development/C
Requires: libpostproc%{libs_suffix}-devel = %version-%release
%filter_from_requires /^\/.*/d






%description -n libavcodec%{libs_suffix}
avcodec library from FFmpeg

%description -n libavcodec%{libs_suffix}-devel
Headers, .pc and .so for libavcodec%{libs_suffix}

%description -n libavcodec%{libs_suffix}-devel-static
.a for libavcodec%{libs_suffix}


%description -n libavformat%{libs_suffix}
avformat library from FFmpeg

%description -n libavformat%{libs_suffix}-devel
Headers, .pc and .so for libavformat%{libs_suffix}

%description -n libavformat%{libs_suffix}-devel-static
.a for libavformat%{libs_suffix}


%description -n libavutil%{libs_suffix}
avutil library from FFmpeg

%description -n libavutil%{libs_suffix}-devel
Headers, .pc and .so for libavutil%{libs_suffix}

%description -n libavutil%{libs_suffix}-devel-static
.a for libavutil%{libs_suffix}


%description -n libavfilter%{libs_suffix}
avfilter library from FFmpeg

%description -n libavfilter%{libs_suffix}-devel
Headers, .pc and .so for libavfilter%{libs_suffix}

%description -n libavfilter%{libs_suffix}-devel-static
.a for libavfilter%{libs_suffix}


%description -n libavdevice%{libs_suffix}
avdevice library from FFmpeg

%description -n libavdevice%{libs_suffix}-devel
Headers, .pc and .so for libavdevice%{libs_suffix}

%description -n libavdevice%{libs_suffix}-devel-static
.a for libavdevice%{libs_suffix}


%description -n libswresample%{libs_suffix}
swresample library from FFmpeg

%description -n libswresample%{libs_suffix}-devel
Headers, .pc and .so for libswresample%{libs_suffix}

%description -n libswresample%{libs_suffix}-devel-static
.a for libswresample%{libs_suffix}


%description -n libswscale%{libs_suffix}
swscale library from FFmpeg

%description -n libswscale%{libs_suffix}-devel
Headers, .pc and .so for libswscale%{libs_suffix}

%description -n libswscale%{libs_suffix}-devel-static
.a for libswscale%{libs_suffix}


%description -n libavresample%{libs_suffix}
avresample library from FFmpeg

%description -n libavresample%{libs_suffix}-devel
Headers, .pc and .so for libavresample%{libs_suffix}

%description -n libavresample%{libs_suffix}-devel-static
.a for libavresample%{libs_suffix}


%description -n libpostproc%{libs_suffix}
postproc library from FFmpeg

%description -n libpostproc%{libs_suffix}-devel
Headers, .pc and .so for libpostproc%{libs_suffix}

%description -n libpostproc%{libs_suffix}-devel-static
.a for libpostproc%{libs_suffix}







%files -n libavcodec%{libs_suffix}
%_libdir/libavcodec%{libs_suffix}.so.*

%files -n libavcodec%{libs_suffix}-devel
/usr/include/libavcodec%{libs_suffix}
%_libdir/libavcodec%{libs_suffix}.so
%_libdir/pkgconfig/libavcodec%{libs_suffix}.pc

%files -n libavcodec%{libs_suffix}-devel-static
%_libdir/libavcodec%{libs_suffix}.a


%files -n libavformat%{libs_suffix}
%_libdir/libavformat%{libs_suffix}.so.*

%files -n libavformat%{libs_suffix}-devel
/usr/include/libavformat%{libs_suffix}
%_libdir/libavformat%{libs_suffix}.so
%_libdir/pkgconfig/libavformat%{libs_suffix}.pc

%files -n libavformat%{libs_suffix}-devel-static
%_libdir/libavformat%{libs_suffix}.a


%files -n libavutil%{libs_suffix}
%_libdir/libavutil%{libs_suffix}.so.*

%files -n libavutil%{libs_suffix}-devel
/usr/include/libavutil%{libs_suffix}
%_libdir/libavutil%{libs_suffix}.so
%_libdir/pkgconfig/libavutil%{libs_suffix}.pc

%files -n libavutil%{libs_suffix}-devel-static
%_libdir/libavutil%{libs_suffix}.a


%files -n libavfilter%{libs_suffix}
%_libdir/libavfilter%{libs_suffix}.so.*

%files -n libavfilter%{libs_suffix}-devel
/usr/include/libavfilter%{libs_suffix}
%_libdir/libavfilter%{libs_suffix}.so
%_libdir/pkgconfig/libavfilter%{libs_suffix}.pc

%files -n libavfilter%{libs_suffix}-devel-static
%_libdir/libavfilter%{libs_suffix}.a


%files -n libavdevice%{libs_suffix}
%_libdir/libavdevice%{libs_suffix}.so.*

%files -n libavdevice%{libs_suffix}-devel
/usr/include/libavdevice%{libs_suffix}
%_libdir/libavdevice%{libs_suffix}.so
%_libdir/pkgconfig/libavdevice%{libs_suffix}.pc

%files -n libavdevice%{libs_suffix}-devel-static
%_libdir/libavdevice%{libs_suffix}.a


%files -n libswresample%{libs_suffix}
%_libdir/libswresample%{libs_suffix}.so.*

%files -n libswresample%{libs_suffix}-devel
/usr/include/libswresample%{libs_suffix}
%_libdir/libswresample%{libs_suffix}.so
%_libdir/pkgconfig/libswresample%{libs_suffix}.pc

%files -n libswresample%{libs_suffix}-devel-static
%_libdir/libswresample%{libs_suffix}.a


%files -n libswscale%{libs_suffix}
%_libdir/libswscale%{libs_suffix}.so.*

%files -n libswscale%{libs_suffix}-devel
/usr/include/libswscale%{libs_suffix}
%_libdir/libswscale%{libs_suffix}.so
%_libdir/pkgconfig/libswscale%{libs_suffix}.pc

%files -n libswscale%{libs_suffix}-devel-static
%_libdir/libswscale%{libs_suffix}.a


%files -n libavresample%{libs_suffix}
%_libdir/libavresample%{libs_suffix}.so.*

%files -n libavresample%{libs_suffix}-devel
/usr/include/libavresample%{libs_suffix}
%_libdir/libavresample%{libs_suffix}.so
%_libdir/pkgconfig/libavresample%{libs_suffix}.pc

%files -n libavresample%{libs_suffix}-devel-static
%_libdir/libavresample%{libs_suffix}.a


%files -n libpostproc%{libs_suffix}
%_libdir/libpostproc%{libs_suffix}.so.*

%files -n libpostproc%{libs_suffix}-devel
/usr/include/libpostproc%{libs_suffix}
%_libdir/libpostproc%{libs_suffix}.so
%_libdir/pkgconfig/libpostproc%{libs_suffix}.pc

%files -n libpostproc%{libs_suffix}-devel-static
%_libdir/libpostproc%{libs_suffix}.a






%package -n ffmpeg-renamed-libs
Summary: FFmpeg libraries, with suffix "%{libs_suffix}" added to all libs and their folders in /usr/include, to avoid conflict with libav:  avcodec avformat avutil avfilter avdevice swresample swscale avresample postproc
Group: System/Libraries
Requires: libavcodec%{libs_suffix}
Requires: libavformat%{libs_suffix}
Requires: libavutil%{libs_suffix}
Requires: libavfilter%{libs_suffix}
Requires: libavdevice%{libs_suffix}
Requires: libswresample%{libs_suffix}
Requires: libswscale%{libs_suffix}
Requires: libavresample%{libs_suffix}
Requires: libpostproc%{libs_suffix}



%description -n ffmpeg-renamed-libs
FFmpeg libraries, with suffix "%{libs_suffix}"
added to all libs and their folders
in /usr/include, to avoid conflict with libav:
  - avcodec
  - avformat
  - avutil
  - avfilter
  - avdevice
  - swresample
  - swscale
  - avresample
  - postproc



%files -n ffmpeg-renamed-libs




%package -n ffmpeg-renamed-libs-devel
Summary: Development files for FFmpeg libs:  avcodec avformat avutil avfilter avdevice swresample swscale avresample postproc
Group: Development/C
Requires: libavcodec%{libs_suffix}-devel
Requires: libavformat%{libs_suffix}-devel
Requires: libavutil%{libs_suffix}-devel
Requires: libavfilter%{libs_suffix}-devel
Requires: libavdevice%{libs_suffix}-devel
Requires: libswresample%{libs_suffix}-devel
Requires: libswscale%{libs_suffix}-devel
Requires: libavresample%{libs_suffix}-devel
Requires: libpostproc%{libs_suffix}-devel



%description -n ffmpeg-renamed-libs-devel
Development files for FFmpeg libraries:
  - avcodec
  - avformat
  - avutil
  - avfilter
  - avdevice
  - swresample
  - swscale
  - avresample
  - postproc



%files -n ffmpeg-renamed-libs-devel




%package -n ffmpeg-renamed-libs-devel-static
Summary: .a files for FFmpeg libs:  avcodec avformat avutil avfilter avdevice swresample swscale avresample postproc
Group: Development/C
Requires: libavcodec%{libs_suffix}-devel-static
Requires: libavformat%{libs_suffix}-devel-static
Requires: libavutil%{libs_suffix}-devel-static
Requires: libavfilter%{libs_suffix}-devel-static
Requires: libavdevice%{libs_suffix}-devel-static
Requires: libswresample%{libs_suffix}-devel-static
Requires: libswscale%{libs_suffix}-devel-static
Requires: libavresample%{libs_suffix}-devel-static
Requires: libpostproc%{libs_suffix}-devel-static



%description -n ffmpeg-renamed-libs-devel-static
.a files for FFmpeg libraries:
  - avcodec
  - avformat
  - avutil
  - avfilter
  - avdevice
  - swresample
  - swscale
  - avresample
  - postproc



%files -n ffmpeg-renamed-libs-devel-static




