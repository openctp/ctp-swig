cmake_minimum_required(VERSION 2.8)

project(ctpapi-python)

set(CMAKE_CXX_STANDARD 11)

if (${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    SET(PY_VER "python_value" CACHE STRING "Python Version")
    SET(PY_LIB "python_lib_value" CACHE STRING "Python Lib Version")

    include_directories(${PROJECT_SOURCE_DIR}
        ${PROJECT_SOURCE_DIR}/win64
        D:/pyenv-win/pyenv-win/versions/${PY_VER}/include
        )
    link_directories(${PROJECT_SOURCE_DIR}
        ${PROJECT_SOURCE_DIR}/win64
        D:/pyenv-win/pyenv-win/versions/${PY_VER}/libs
        )
    add_compile_options(/bigobj /MT)
elseif (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    include_directories(${PROJECT_SOURCE_DIR}
        ${PROJECT_SOURCE_DIR}/lin64
        /root/.pyenv/versions/3.12.0/include/python3.12/
        )
    link_directories(${PROJECT_SOURCE_DIR}
        
        /root/.pyenv/versions/3.12.0/lib/
        )
endif()

set(trader _thosttraderapi)
set(mduser _thostmduserapi)

add_library(${trader} SHARED thosttraderapi_wrap.cxx)
if (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set_target_properties(${trader} PROPERTIES POSITION_INDEPENDENT_CODE ON)
    set_target_properties(${trader} PROPERTIES LINK_FLAGS "-Wl,-enable-new-dtags")
    set_target_properties(${trader} PROPERTIES
        SKIP_BUILD_RPATH OFF
        BUILD_WITH_INSTALL_RPATH ON
        INSTALL_RPATH "./")
    add_library(LIB_TD SHARED IMPORTED)
    set_property(TARGET LIB_TD PROPERTY IMPORTED_LOCATION ${PROJECT_SOURCE_DIR}/lin64/thosttraderapi_se.so)
    set_target_properties(${trader} PROPERTIES PREFIX "")
    target_link_libraries(${trader} PUBLIC pthread LIB_TD python3.12)
elseif (${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    target_link_libraries(${trader} PUBLIC "lin64/thosttraderapi_se.so" python3.12)
endif()

add_library(${mduser} SHARED thostmduserapi_wrap.cxx)
if (${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set_target_properties(${mduser} PROPERTIES POSITION_INDEPENDENT_CODE ON)
    set_target_properties(${mduser} PROPERTIES LINK_FLAGS "-Wl,-enable-new-dtags")
    set_target_properties(${mduser} PROPERTIES
        SKIP_BUILD_RPATH OFF
        BUILD_WITH_INSTALL_RPATH ON
        INSTALL_RPATH "./")
    add_library(LIB_MD SHARED IMPORTED)
    set_property(TARGET LIB_MD PROPERTY IMPORTED_LOCATION ${PROJECT_SOURCE_DIR}/lin64/thostmduserapi_se.so)
    set_target_properties(${mduser} PROPERTIES PREFIX "")
    target_link_libraries(${mduser} PUBLIC pthread LIB_MD python3.12)
elseif (${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    target_link_libraries(${mduser} PUBLIC thostmduserapi_se python3.12)
endif()
