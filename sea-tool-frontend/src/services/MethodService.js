import { API_URL } from '@/utils/Constants';
import BaseApiService from './BaseApiService';

const createUrl = ({ id, oId }) => {
	const base = `${API_URL}/organizations/${oId}/methods/`;
	return id ? `${base}${id}/` : base;
};

export default new BaseApiService(createUrl);
