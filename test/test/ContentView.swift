//
//  ContentView.swift
//  test
//
//  Created by Станислав Билим on 28.02.2023.
//

import SwiftUI

struct ContentView: View {
    @Binding var document: testDocument

    var body: some View {
        TextEditor(text: $document.text)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView(document: .constant(testDocument()))
    }
}
