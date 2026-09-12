from setuptools import find_packages, setup

package_name = 'robot_description'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',
            ['launch/display.launch.py']),
        ('share/' + package_name + '/urdf',
            ['urdf/robot.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Siddhesh Adavade',
    maintainer_email='siddheshadavade@todo.todo',
    description='URDF and ROS 2 description package for a 4-axis industrial robot arm.',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [],
    },
)
