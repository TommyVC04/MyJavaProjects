//
//  CancelButton.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 9/28/22.
//

import SwiftUI

struct CancelButton: View {
    @State private var isSet = false

    var body: some View {
        Button (action: {isSet = true} ){
            Text("Cancel")
        }
        .padding()
        .foregroundColor(.gray)
        .background(Color(red: 211.0/255, green: 211.0/255, blue: 211.0/255))
        .clipShape(RoundedRectangle(cornerRadius: 5))
        .confirmationDialog("Are you sure?", isPresented: $isSet, titleVisibility: .visible) {
            Button("Yes", role: .destructive) {
                FavoriteButton()
            }
            Button("Cancel", role: .cancel) {}
        }
    }
}

struct CancelButton_Previews: PreviewProvider {
    static var previews: some View {
        CancelButton()
    }
}
