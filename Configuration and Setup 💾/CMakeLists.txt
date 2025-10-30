Update CMakeLists.txt
Export the urdf, launch, and config directories so ROS 2 can find them.

CMake

# Add the following to your CMakeLists.txt (after the install(TARGETS... block)
```
install(DIRECTORY
  launch
  urdf
  config
  DESTINATION share/${PROJECT_NAME}
)
```
