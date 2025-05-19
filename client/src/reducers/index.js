import { combineReducers } from 'redux';
import { propertiesListReducer } from './propertyReducers';

const rootReducer = combineReducers({
    propertiesList: propertiesListReducer,
});

export default rootReducer;