import React from 'react';
import {useForm} from "react-hook-form";
import {authService} from "../services/authService";
import {useNavigate} from "react-router-dom";

const LoginPage = () => {
    const{handleSubmit, register} = useForm();
    const navigate = useNavigate()
    const onSubmit = async (user)=>{
        await authService.login(user)
        navigate('/cars')
    }

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <input type="text" placeholder='' {...register('email')}/>
            <input type="text" placeholder='' {...register('password')}/>
            <button>Login</button>
        </form>
    );
};

export {LoginPage};