/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

 import React from 'react';
 import {
   View,
   Text,
   StyleSheet,
 } from 'react-native';
 import {
   Provider as PaperProvider,
   Appbar,
   FAB,
   Portal,
 } from 'react-native-paper'
 
 class HomePage extends React.Component {
 
   render() {
     return (
       <View>
         <Portal>
           <Appbar.Header>
             <Appbar.Content title="Counter" />
           </Appbar.Header>
           <View>
           </View>
           <FAB
             style={styles.fab}
             icon="plus"
             color="white"
             onPress={() => {}} />
         </Portal>
       </View>
     )
   }
 }
 
 const App = () => {
   return (
     <PaperProvider>
       <HomePage />
     </PaperProvider>
   );
 };
 
 const styles = StyleSheet.create({
   center: {
     alignItems: 'center',
     justifyContent: 'center',
     height: '100%',
   },
   fab: {
     position: 'absolute',
     margin: 16,
     right: 0,
     bottom: 0,
   },
 })
 
 export default App;
 