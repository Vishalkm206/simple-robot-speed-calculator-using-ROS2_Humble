from setuptools import find_packages, setup

package_name = 'robot_speed'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vishal',
    maintainer_email='vishal@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "rpm_publisher = robot_speed.rpm_pub:main",
            "calc_speed = robot_speed.calculate_speedv:main",
        ],
    },
)
