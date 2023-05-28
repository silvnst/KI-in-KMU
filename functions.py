def plot_variable_importance(model, X_train, model_name, artikel_name):
    import matplotlib.pyplot as plt
    from pandas import DataFrame
    from sklearn.ensemble import VotingRegressor

    if isinstance(model, VotingRegressor):
        for i, m in enumerate(model.estimators_):
            plot_variable_importance(m, X_train, f"Estimator {i}", artikel_name)
    else:
        if model_name == 'LinearRegression':
            imp=DataFrame({"imp":model.coef_, "names":X_train.columns}).sort_values("imp", ascending=True)
            title = 'Coefficients Plot ' + artikel_name + ' ' + model_name
        elif hasattr(model, "feature_importances_"):
            imp=DataFrame({"imp":model.feature_importances_, "names":X_train.columns}).sort_values("imp", ascending=True)
            title = 'Variable Importance Plot ' + artikel_name + ' ' + model_name
        else:
            print(f"No feature importances or coefficients available for model {model_name}")
            return
            
        fig, ax = plt.subplots(figsize=(15, 5), dpi=150) 
        ax.barh(imp["names"],imp["imp"], color="green") 
        ax.set_xlabel('\nVariable Importance/Coefficients')
        ax.set_ylabel('Features\n') 
        ax.set_title(title + '\n') 
        plt.show()