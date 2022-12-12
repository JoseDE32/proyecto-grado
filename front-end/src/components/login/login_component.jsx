import React, {useState} from 'react';
import axios from 'axios';
import {Container, Row, Col, Button} from "react-bootstrap";
import Form from 'react-bootstrap/Form';
import App from '../../App.js'
import Footer from '../componentes_generales/footer.jsx';

const login_component = () =>{

  const [state,set_state] = useState({
    usuario: '',
    contrasena: '',
    logged:true,
  })
  const url = "http://127.0.0.1:8000/login" 
  const data = {
    'username' : state.usuario[0],
    'password' : state.contrasena[0]
  }

  const handle_user = (e) => {
    set_state({
      ...state,
      usuario : [e.target.value],
    })

  }
  const handle_password = (e) => {
    console.log(e)
    set_state({
      ...state,
      contrasena : [e.target.value],
    })

  }
  const handleSendNewData = () => {
    axios.post(url, data)
    .then(res=>{
      console.log(res.data)
      localStorage.setItem('token', res.data.token)
      localStorage.setItem('refresh-token', res.data['refresh-token'])
      localStorage.setItem('email', res.data.user.email)
      localStorage.setItem('first_name', res.data.user.first_name)
      localStorage.setItem('instancia', res.data.user.instancia)
      localStorage.setItem('last_name', res.data.user.last_name)
      localStorage.setItem('nombre_completo', res.data.user.nombre_completo)
      localStorage.setItem('instancia_id', res.data.user.instancia_id)
      localStorage.setItem('rol', res.data.user.rol)
      localStorage.setItem('semestre_actual', res.data.user.semestre_actual)
      localStorage.setItem('username', res.data.user.username)
      localStorage.setItem('message', res.data.user.message)
    })
    .catch(err=>console.log(err))
    set_state({
      ...state,
      logged:false,
    })
  }

  return (
    <Row>
      {
        state.logged ?
        (
          <Container className="containerLogin">
            <Row>
            <Col>
              <Row>
                <h2 className='title_login'>
                  <b>Universidad del Valle</b>
                </h2>
              </Row>
              <Row>
                <h3 className='title_login'>
                  Sistema ASES
                </h3>
              </Row>
            </Col>
            <Col>
              <div className="formularioLogin">
                <Row className="form_title">
                  <h3><b>Sing In</b></h3>
                </Row>
                <div className="form_login">
                  <div className="form_group_login">
                    <Form.Control className='form_input_login' id='user' type="text" onChange={handle_user} placeholder=" "/>
                    <label className='form_label_login' for="user">Usuario</label>
                  </div>
                  <div className="form_group_login">
                    <Form.Control className='form_input_login' id='pass' type="password" onChange={handle_password} placeholder=" "/>
                    <label className='form_label_login' for="pass">Contraseña</label>
                  </div>
                </div>
                <Row className='mt-2'> 
                  <Button onClick={handleSendNewData}>Ingresar</Button> 
                </Row>
              </div>
            </Col>
            </Row>
          </Container>
        )
        :
        (
          <App/>
        )
      } 
    </Row>
  )
}

export default login_component