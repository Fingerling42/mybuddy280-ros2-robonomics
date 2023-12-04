from setuptools import find_packages, setup

package_name = 'mybuddy280_driver'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ivan Berman',
    maintainer_email='berman@robonomics.network',
    description='Driver for myBuddy 280 two-arm manipulator based on pymycobot, credits to Elephant Robotics.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mybuddy280_ros_wrapper = mybuddy280_driver.mybuddy280_ros2_wrapper:main',
        ],
    },
)