cmake_minimum_required(VERSION 3.15)
project(cpp_method)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(method)

add_executable(beamforming
        method/delay_and_sum.hpp
        method/NDAS.hpp
        method/NRDAS.hpp
        method/optimized_reversed_method.hpp
        method/reversed_method.hpp
        method/reversed_synthetic_aperture.hpp
        method/RSA.hpp
        method/RSA_deduction.hpp
        method/RSA_linear_approximation.hpp
        method/stream_reversed_method.hpp
        method/synthetic_aperture.hpp
        args.hpp
        beamforming.cpp
        func.hpp
        json.hpp
        para.hpp)
