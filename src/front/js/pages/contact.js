import React, { useState, useEffect, useContext } from "react";
import PropTypes from "prop-types";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";

export const Contact = (props) => {
  const { store, actions } = useContext(Context);
  const params = useParams();
    return (
    <div className="container mx-auto" >
      <div className="form-body">
        <div className="row">
          <div className="form-holder">
            <div className="form-content ">
              <div className="form-items">
                 <h3 className="text-center">Contacto</h3>
                 <p className="text-center mb-0">¿Necesitas ayuda?</p>
                 <p className="text-center mt-0">Ponte en contacto con nosotros</p>
                <div className="card col-xs-4 col-sm-4 col-md-4 col-lg-6 col-xl-6" id="card">
                <form className="requires-validation" novalidate>
                <h3 className="text-center mt-3" id="iconbutton">Escríbenos</h3>
                  <div className="col ms-3 me-3">
                    <label for="basic-url" className="form-label mt-0 mb-0">Nombre y Apellidos</label>
                    <input
                    className="form-control"
                    type="text"
                    name="name"
                    required
                    />
                    <div className="valid-feedback">
                    Campo nombre y apellidos es válido.
                    </div>
                    <div className="invalid-feedback">
                    Campo nombre y apellidos no puede estar en blanco.
                  </div>
                  </div>
                  <div className="col ms-3 me-3">
                    <label for="basic-url" className="form-label mt-3 mb-0">Email</label>
                    <input
                    className="form-control"
                    type="email"
                    name="email"
                    required
                    />
                    <div className="valid-feedback">Campo Email es válido.</div>
                    <div className="invalid-feedback">
                    Campo Email no puede estar en blanco.
                    </div>
                  </div>
                  <div className="col ms-3 me-3">
                    <label for="basic-url" className="form-label mt-3 mb-0">Teléfono</label>
                    <input
                    className="form-control"
                    type="telefono"
                    name="Teléfono"
                    required
                    />
                    <div className="valid-feedback">Campo Teléfono es válido</div>
                    <div className="invalid-feedback">
                    Campo Teléfono no puede estar en blanco
                    </div>
                  </div>
                  <div className="col ms-3 me-3">
                    <label for="basic-url" className="form-label mt-3 mb-0">Tema de consulta</label>
                    <select className="form-select mt-0" required>
                      <option selected disabled value="">Hacerme Gestor </option>
                      <option value="jweb">Información sobre Baby Friendly</option>
                      <option value="sweb">Claves de acceso</option>
                      <option value="pmanager">Otras consultas</option>
                    </select>
                    <div className="valid-feedback">
                    Has seleccionado un asunto.</div>
                    <div className="invalid-feedback">
                    Por favor, selecciona un asunto.
                    </div>
                    </div>
                  <div className="col ms-3 me-3">
                    <label for="basic-url" className="form-label mt-3 mb-0">Comentarios</label>
                    <input id="commentinput"
                    className="form-control"
                    type="text"
                    name="Comentarios"
                    required
                    />
                    <div className="valid-feedback">
                    Campo Comentarios es válido</div>
                    <div className="invalid-feedback">
                    Campo Comentarios no puede estar en blanco
                    </div>
                  </div>
                  <div className="form-check col mt-3 ms-3 me-3">
                    <input
                    className="form-check-input"
                    type="checkbox"
                    value=""
                    id="invalidCheck"
                    required
                    />
                    <label className="form-check-label"> Confirmo que he leido y acepto la Política de Privacidad y Aviso Legal.</label>
                    <div className="invalid-feedback">
                    Por favor, confirma que has leido y aceptas la Política de Privacidad y Aviso Legal.
                    </div>
                  </div>
                  <div className="form-button mt-3 ms-3 me-3 mb-3">
                    <button id="button" type="submit" className="btn btn-primary">
                    Enviar
                    </button>
                  </div>
                </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );};