from setuptools import find_packages, setup

package_name = 'oled_display'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='quanghuy',
    maintainer_email='quanghuy2kx@gmail.com',
    description='ROS2 package for OLED display control based on /cmd_vel',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'oled_display_node = oled_display.oled_display_node:main'
        ],
    },
)
