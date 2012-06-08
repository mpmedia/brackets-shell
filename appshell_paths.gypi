# Copyright (c) 2011 The Chromium Embedded Framework Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'includes': [
    # Bring in the autogenerated source file lists.
    'cef_paths.gypi',
   ],
  'variables': {
    'includes_common': [
      'include/cef_base.h',
      'include/cef_pack_resources.h',
      'include/cef_pack_strings.h',
      'include/cef_runnable.h',
      'include/cef_version.h',
      'include/internal/cef_build.h',
      'include/internal/cef_export.h',
      'include/internal/cef_ptr.h',
      'include/internal/cef_string.h',
      'include/internal/cef_string_list.h',
      'include/internal/cef_string_map.h',
      'include/internal/cef_string_multimap.h',
      'include/internal/cef_string_types.h',
      'include/internal/cef_string_wrappers.h',
      'include/internal/cef_time.h',
      'include/internal/cef_tuple.h',
      'include/internal/cef_types.h',
      'include/internal/cef_types_wrappers.h',
      '<@(autogen_cpp_includes)',
    ],
    'includes_capi': [
      'include/capi/cef_base_capi.h',
      '<@(autogen_capi_includes)',
    ],
    'includes_wrapper': [
      'include/wrapper/cef_byte_read_handler.h',
      'include/wrapper/cef_stream_resource_handler.h',
      'include/wrapper/cef_xml_object.h',
      'include/wrapper/cef_zip_archive.h',
    ],
    'includes_win': [
      'include/internal/cef_types_win.h',
      'include/internal/cef_win.h',
    ],
    'includes_mac': [
      'include/cef_application_mac.h',
      'include/internal/cef_mac.h',
      'include/internal/cef_types_mac.h',
    ],
    'includes_linux': [
      'include/internal/cef_linux.h',
      'include/internal/cef_types_linux.h',
    ],
    'libcef_sources_common': [
      'libcef_dll/cef_logging.h',
      'libcef_dll/cpptoc/cpptoc.h',
      'libcef_dll/ctocpp/ctocpp.h',
      'libcef_dll/libcef_dll.cc',
      'libcef_dll/libcef_dll2.cc',
      'libcef_dll/resource.h',
      'libcef_dll/transfer_util.cpp',
      'libcef_dll/transfer_util.h',
      '<@(autogen_library_side)',
    ],
    'libcef_dll_wrapper_sources_common': [
      'libcef_dll/cef_logging.h',
      'libcef_dll/cpptoc/base_cpptoc.h',
      'libcef_dll/cpptoc/cpptoc.h',
      'libcef_dll/ctocpp/base_ctocpp.h',
      'libcef_dll/ctocpp/ctocpp.h',
      'libcef_dll/transfer_util.cpp',
      'libcef_dll/transfer_util.h',
      'libcef_dll/wrapper/cef_byte_read_handler.cc',
      'libcef_dll/wrapper/cef_stream_resource_handler.cc',
      'libcef_dll/wrapper/cef_xml_object.cc',
      'libcef_dll/wrapper/cef_zip_archive.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper2.cc',
      '<@(autogen_client_side)',
    ],
    'appshell_sources_common': [
      'appshell/appshell_extensions.cpp',
      'appshell/appshell_extensions.h',
      'appshell/config.h',
      'appshell/cefclient.cpp',
      'appshell/cefclient.h',
      'appshell/client_app.cpp',
      'appshell/client_app.h',
      'appshell/client_app_delegates.cpp',
      'appshell/client_handler.cpp',
      'appshell/client_handler.h',
      'appshell/client_switches.cpp',
      'appshell/client_switches.h',
      'appshell/resource_util.h',
      'appshell/string_util.cpp',
      'appshell/string_util.h',
      'appshell/util.h',
    ],
    'appshell_sources_win': [
      'appshell/cefclient.rc',
      'appshell/cefclient_win.cpp',
      'appshell/client_handler_win.cpp',
      'appshell/resource.h',
      'appshell/res/cefclient.ico',
      'appshell/res/logoball.png',
      'appshell/res/small.ico',
      'appshell/resource_util_win.cpp',
    ],
    'appshell_sources_mac': [
      'appshell/cefclient_mac.mm',
      'appshell/client_handler_mac.mm',
      'appshell/resource_util_mac.mm',
    ],
    'appshell_sources_mac_helper': [
      'appshell/appshell_extensions.cpp',
      'appshell/appshell_extensions.h',
      'appshell/client_app.cpp',
      'appshell/client_app.h',
      'appshell/client_app_delegates.cpp',
      'appshell/client_handler.cpp',
      'appshell/client_handler.h',
      'appshell/client_handler_mac.mm',
      'appshell/client_switches.cpp',
      'appshell/client_switches.h',
      'appshell/process_helper_mac.cpp',
      'appshell/resource_util.h',
      'appshell/resource_util_mac.mm',
      'appshell/string_util.cpp',
      'appshell/string_util.h',
      'appshell/util.h',
    ],
    'appshell_bundle_resources_mac': [
      'appshell/mac/cefclient.icns',
      'appshell/mac/English.lproj/InfoPlist.strings',
      'appshell/mac/English.lproj/MainMenu.xib',
      'appshell/mac/Info.plist',
    ],
    'appshell_sources_linux': [
      'appshell/cefclient_gtk.cpp',
      'appshell/client_handler_gtk.cpp',
      'appshell/resource_util_linux.cpp',
    ],
    'appshell_bundle_resources_linux': [
    ],
  },
}
