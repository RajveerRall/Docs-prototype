# Additional Information







Utils functions summary Data Storage Utilities

this.utils.dataStore: Stores and retrieves data for page references.

Methods: getData(key), setData(key, value), clearData().

this.utils.context: Passes data between pages.

Methods: getDataMap(object), setData(object, key, data), getData(object, key).

Third-Party Libraries



this.utils.FileSaver: Uses the file-saver library for file operations.

this.utils.dateFormat: Uses the dateformat library for formatting dates.



Navigation Utilities



this.utils.navigateTo(appId, pageId, data, object): Navigates to a specific page within an app (object should be this).

this.utils.navigateToCurrAppPages(pageId, data, object): Navigates within the current app pages.

this.utils.getNavigatedData(key, object): Retrieves data passed between pages.

Security and Role Management



this.utils.RSAUtil: Encrypts passwords.

Methods: convertJwkToPem(jwk), encrypt(text, pubKey, keyFormat).

this.utils.RolesUtils: Manages user roles for filtering navigators in preview mode.

Methods: delete(role, userDomain), set(role, userDomain), getRoles(), clear(), saveRoles(roles, userDomain).



Utility Functions



this.utils.getUrlParams(): Retrieves URL parameters.

this.utils.hasSuperAdminPrivilege(): Checks if the current user is a super admin.

this.utils.getAssetsUrl(assetsName, fileName): Retrieves asset file URLs.

this.utils.handleProfile: Used to do virtual login with profile in preview, only work in preview and will not generate in runtime.

Methods: handleProfile(data: {

userDomainCode: string; userAccountId: string; vault: string }).

Note: * indicates different implementations between designer mode and runtime mode.



