#!/bin/bash

libs="avcodec avformat avutil avfilter avdevice swresample swscale avresample postproc"
echo -en "\\n\\n\\n####### AUTOMATICALLY GENERATED PART ######\\n"
echo -en "\\n\\n"



for i in $libs ; do
  echo %package -n lib${i}%{libs_suffix}
  echo Summary: ${i} library from FFmpeg
  echo Group: System/Libraries
  echo %filter_from_requires /^\\/.\*/d
  echo
  echo %package -n lib${i}%{libs_suffix}-devel
  echo Summary: Headers, .pc and .so for lib${i}%{libs_suffix}
  echo Group: Development/C
  echo Requires: lib${i}%{libs_suffix} = %version-%release
  echo %filter_from_requires /^\\/.\*/d
  echo
  echo %package -n lib${i}%{libs_suffix}-devel-static
  echo Summary: .a for lib${i}%{libs_suffix}
  echo Group: Development/C
  echo Requires: lib${i}%{libs_suffix}-devel = %version-%release
  echo %filter_from_requires /^\\/.\*/d
  echo
done




echo -en "\\n\\n\\n\\n\\n"

for i in $libs ; do
  echo %description -n lib${i}%{libs_suffix}
  echo ${i} library from FFmpeg
  echo
  echo %description -n lib${i}%{libs_suffix}-devel
  echo Headers, .pc and .so for lib${i}%{libs_suffix}
  echo
  echo %description -n lib${i}%{libs_suffix}-devel-static
  echo .a for lib${i}%{libs_suffix}
  echo -en "\\n\\n"
done


echo -en "\\n\\n\\n\\n\\n"

for i in $libs ; do
  echo %files -n lib${i}%{libs_suffix}
  echo %_libdir/lib${i}%{libs_suffix}.so.*
  echo
  echo %files -n lib${i}%{libs_suffix}-devel
  echo /usr/include/lib${i}%{libs_suffix}
  echo %_libdir/lib${i}%{libs_suffix}.so
  echo %_libdir/pkgconfig/lib${i}%{libs_suffix}.pc
  echo
  echo %files -n lib${i}%{libs_suffix}-devel-static
  echo %_libdir/lib${i}%{libs_suffix}.a
  echo -en "\\n\\n"
done


echo -e "\\n\\n\\n"

echo "%package -n ffmpeg-renamed-libs"
echo -n "Summary: FFmpeg libraries, with suffix \"%{libs_suffix}\" added to all libs and their folders in /usr/include, to avoid conflict with libav: "
for i in $libs ; do
  echo -n " $i"
done
echo -e "\\nGroup: System/Libraries"
for i in $libs ; do
  echo "Requires: lib${i}%{libs_suffix}"
done
echo -e "\\n\\n"
echo "%description -n ffmpeg-renamed-libs"
echo -e "FFmpeg libraries, with suffix \"%{libs_suffix}\"\\nadded to all libs and their folders\\nin /usr/include, to avoid conflict with libav:"
for i in $libs ; do
  echo "  - ${i}"
done
echo -e "\\n\\n"
echo "%files -n ffmpeg-renamed-libs"
echo -e "\\n\\n\\n"



echo "%package -n ffmpeg-renamed-libs-devel"
echo -n "Summary: Development files for FFmpeg libs: "
for i in $libs ; do
  echo -n " $i"
done
echo -e "\\nGroup: Development/C"
for i in $libs ; do
  echo "Requires: lib${i}%{libs_suffix}-devel"
done
echo -e "\\n\\n"
echo "%description -n ffmpeg-renamed-libs-devel"
echo "Development files for FFmpeg libraries:"
for i in $libs ; do
  echo "  - ${i}"
done
echo -e "\\n\\n"
echo "%files -n ffmpeg-renamed-libs-devel"
echo -e "\\n\\n\\n"


echo "%package -n ffmpeg-renamed-libs-devel-static"
echo -n "Summary: .a files for FFmpeg libs: "
for i in $libs ; do
  echo -n " $i"
done
echo -e "\\nGroup: Development/C"
for i in $libs ; do
  echo "Requires: lib${i}%{libs_suffix}-devel-static"
done
echo -e "\\n\\n"
echo "%description -n ffmpeg-renamed-libs-devel-static"
echo ".a files for FFmpeg libraries:"
for i in $libs ; do
  echo "  - ${i}"
done
echo -e "\\n\\n"
echo "%files -n ffmpeg-renamed-libs-devel-static"
echo -e "\\n\\n\\n"
