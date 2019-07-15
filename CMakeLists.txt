cmake_minimum_required(VERSION 2.8.3)
project(LapAI)


link_directories(/usr/lib)
link_directories(/home/abhijeet/.local/lib/python2.7)
find_package(
   OpenCV REQUIRED
)

macro(add_python_target tgt)
  foreach(file ${ARGN})
    set(OUT ${CMAKE_CURRENT_BINARY_DIR}/${file}.pyo)
    list(APPEND OUT_FILES ${OUT})
    add_custom_command(OUTPUT ${OUT}
        COMMAND <python command you use to byte-compile .py file>)
  endforeach()

  add_custom_target(${tgt} ALL DEPENDS ${OUT_FILES})
endmacro()


include_directories(include)

#file(GLOB SOURCES "src/*.cpp")

add_python_target(exe scripts/Mouse_swing.py)
#target_link_libraries(exe ${OpenCV_LIBS})
