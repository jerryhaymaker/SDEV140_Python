<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class FinalExam
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.txtNumInput = New System.Windows.Forms.TextBox()
        Me.lblNumInput = New System.Windows.Forms.Label()
        Me.btnDoubleIntegerInput = New System.Windows.Forms.Button()
        Me.btnHalfIntegerInput = New System.Windows.Forms.Button()
        Me.SuspendLayout()
        '
        'txtNumInput
        '
        Me.txtNumInput.Location = New System.Drawing.Point(136, 56)
        Me.txtNumInput.Name = "txtNumInput"
        Me.txtNumInput.Size = New System.Drawing.Size(100, 20)
        Me.txtNumInput.TabIndex = 0
        '
        'lblNumInput
        '
        Me.lblNumInput.AutoSize = True
        Me.lblNumInput.Location = New System.Drawing.Point(33, 56)
        Me.lblNumInput.Name = "lblNumInput"
        Me.lblNumInput.Size = New System.Drawing.Size(97, 15)
        Me.lblNumInput.TabIndex = 1
        Me.lblNumInput.Text = "Enter an integer:"
        '
        'btnDoubleIntegerInput
        '
        Me.btnDoubleIntegerInput.Location = New System.Drawing.Point(36, 103)
        Me.btnDoubleIntegerInput.Name = "btnDoubleIntegerInput"
        Me.btnDoubleIntegerInput.Size = New System.Drawing.Size(75, 23)
        Me.btnDoubleIntegerInput.TabIndex = 2
        Me.btnDoubleIntegerInput.Text = "DOUBLE"
        Me.btnDoubleIntegerInput.UseVisualStyleBackColor = True
        '
        'btnHalfIntegerInput
        '
        Me.btnHalfIntegerInput.Location = New System.Drawing.Point(145, 103)
        Me.btnHalfIntegerInput.Name = "btnHalfIntegerInput"
        Me.btnHalfIntegerInput.Size = New System.Drawing.Size(75, 23)
        Me.btnHalfIntegerInput.TabIndex = 3
        Me.btnHalfIntegerInput.Text = "HALF"
        Me.btnHalfIntegerInput.UseVisualStyleBackColor = True
        '
        'FinalExam
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(284, 259)
        Me.Controls.Add(Me.btnHalfIntegerInput)
        Me.Controls.Add(Me.btnDoubleIntegerInput)
        Me.Controls.Add(Me.lblNumInput)
        Me.Controls.Add(Me.txtNumInput)
        Me.Name = "FinalExam"
        Me.Text = "Jerry Haymaker"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents txtNumInput As TextBox
    Friend WithEvents lblNumInput As Label
    Friend WithEvents btnDoubleIntegerInput As Button
    Friend WithEvents btnHalfIntegerInput As Button
End Class
