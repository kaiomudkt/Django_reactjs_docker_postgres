import { getAuthTokenUserLogged } from '../user.api';
import axios from 'axios';

export const environmentVariables = () => {
    const environment = {
        baseUrl: process.env.BACKEND_BASE_URL        || "localhost",
        // versionApi: process.env.BACKEND_API_VERSION  || "v1",
        versionApi: process.env.BACKEND_API_VERSION  || "",
        typeEnviroment: process.env.TYPE_ENVIROMENT  || "DEVELOPMENT",
        methodHttp: process.env.BACKEND_METHOD_HTTP  || "http",
        backendPort: process.env.BACKEND_PORT        || "3001",
        frontendPort: process.env.FRONTEND_PORT      || "8080",
    };
    return environment;
}

/**
 * @var jwt token de autenticacao do usuario logado
 * @var env variaveis de ambiente 
 * @var baseUrlRequest string para acessar a url base da aplicação backend, que deve ser concatenada com o recurso desejado por cada request
 * @returns Objeto com as configurações para o axios
 */
const getConfigAxios = () => {
    const jwt = getAuthTokenUserLogged();
    const env = environmentVariables();
    const baseUrlRequest = `${env.methodHttp}://${env.baseUrl}:${env.backendPort}/${env.versionApi}/`;
    const config = {
        headers: {
          Authorization: `Bearer ${jwt}`,
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        //   'Access-Control-Allow-Origin': '*',
        },
        withCredentials: true, // Configuração para enviar cookies
        params: {
            language: "pt-BR",
            page: 1,
        },
        baseURL: baseUrlRequest,
    };
    return config;
};

/**
 * returna instancia do axios já configurada
 * para ser usada nas requisições para o backend
 */
export const getInstanceAxios = () => {
    const configAxios = getConfigAxios();
    const instanceAxios = axios.create(configAxios);
    return instanceAxios;
};
